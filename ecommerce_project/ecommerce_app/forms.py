from django import forms
from django.contrib.auth.models import User
from ecommerce_app.models import Cart, orders

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            "last_name":forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            "email":forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            "password":forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password'] 
        widgets= {
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            "password":forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        }
       
class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['quantity']
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control','max':10})
        }
class OrderForm(forms.ModelForm):  
    class Meta:
        model=orders
        fields=['email','address'] 
        widgets= {
            "email":forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            "address":forms.Textarea(attrs={'class':'form-control','placeholder':'Address'})
        }     
        