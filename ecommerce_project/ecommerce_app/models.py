from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator



class Category(models.Model):
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
        

    def __str__(self):
        return self.name


class Products(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=250)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="media",null=True)


    def __str__(self):
        return self.product_name  

class Cart(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)      
    user=models.ForeignKey(User,on_delete=models.CASCADE)      
    quantity=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(10)]) 
    options=(
        ('in-cart','in-cart'),
        ('order-placed','order-placed'),
        ('cancelled','cancelled'),
    )
    status=models.CharField(max_length=100,choices=options,default="in-cart")
    total=models.IntegerField(default=0)

class orders(models.Model):
    product=models.ForeignKey(Cart,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    email=models.EmailField()
    address=models.TextField(max_length=250)
    options=(
        ('order-placed','order-placed'),
        ('cancelled','cancelled'),
        ('dispatched','dispatched'),
        ('delivered','delivered')
    ) 
    status=models.CharField(max_length=100,choices=options,default='order-placed')   
       