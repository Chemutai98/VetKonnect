from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
   ('vc', 'vanilla cake'),
   ('cc', 'chocolate cake'),
   ('cmc', 'choco-mint cake'),
   ('sc', 'strawberry cake'),
   ('bc', 'blueberry cake'),
   ('oc', 'orange cake'),
   ('pc', 'pinacollada cake'),
   ('passc', 'passion cake'),
)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField() 
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    products_image = models.ImageField(upload_to='products')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50) 
    mobile = models.IntegerField(default=0)
    
    def __str__(self):   
        return self.name