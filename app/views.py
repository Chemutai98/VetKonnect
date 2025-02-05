from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0]).category.values('title')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
            return render(request, "app/customerregistration.html", locals())
        else:
            messages.warning(request, "Invalid Input Data")
            return render(request, "app/customerregistration.html", locals())

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "app/profile.html", locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            mobile = form.cleaned_data['mobile']
            city = form.cleaned_data['city']

            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city)
            reg.save()
            messages.success(request, "Congratulations! Profile saved successfully")
            return render(request, "app/profile.html", locals())
        else:
            messages.warning(request, "Invalid Input Data")
            return render(request, "app/profile.html", locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "app/address.html", locals()) 

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, "app/updateAddress.html", locals()) 

        pass
    def post(self, request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.mobile = form.cleaned_data['mobile']
            add.city = form.cleaned_data['city']
            add.save()
            messages.success(request, "Congratulations! Profile Updated Successfuly")
        else:
            messages.warning(request, "Invalid Input Data")

        return redirect("address")