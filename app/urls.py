from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryView, CustomerRegistrationView, CategoryTitle, ProductDetail, ProfileView
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>/', CategoryView.as_view(), name='category'),
    path('category-title/<val>/', CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    
    
    

    # login authentication
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('accounts/profile/', ProfileView.as_view(), name='accounts-profile'), 
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),  name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
