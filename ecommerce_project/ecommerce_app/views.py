from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.core.mail import send_mail,settings
from .forms import RegisterForm,LoginForm,CartForm,OrderForm
from .models import Category,Products,Cart, orders
from ecommerce_app.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class Home(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs): 
        context=super().get_context_data(**kwargs)
        context["product"]=Products.objects.all()
        return context
    # def get(self,request):
    #     return render(request,'index.html')      
class RegisterView(CreateView):
    model=User
    form_class=RegisterForm
    template_name='register.html'
    # success_url=reverse_lazy('home_view')

    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect('home_view')
class LoginView(View):
    def get(self,request,*args,**kwarg):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*arg,**kwargs):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(self.request,"Login successful")
            return redirect('home_view')
        else:
            messages.success(self.request,"invalid credentials")
            return redirect('home_view')
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login_view')
class Productdetail(DetailView):
    model=Products
    template_name='detail.html'
    context_object_name='product'  
    pk_url_kwarg='id'

class AddCartView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        form=CartForm()
        return render(request,'add_to_cart.html',{'product':product,'form':form})
    def post(self,request,*args,**kwargs):
        product=Products.objects.get(id=kwargs.get("id"))
        user=request.user
        if user.is_authenticated:
          cart_data=Cart.objects.filter(user=request.user,products=product)
          quantity=int(request.POST.get('quantity'))
          if cart_data:
            if cart_data[0].status=="order-placed":
                price=cart_data[0].products.price
                Cart.objects.create(product=product,user=user,quantity=quantity,total=quantity*price)
                messages.success(request,'product added successfully')
                return redirect('home_view')
            elif cart_data[0].status=="in-cart":
                pro=cart_data[0]
                pro.quantity+=quantity
                # pro.total+=pro.quantity*pro.products.price
                pro.total=pro.quantity*pro.products.price
                pro.save()
                messages.success(request,'product added successfully')
                return redirect('home_view')
          else:
        # quantity=request.POST.get('quantity')
           Cart.objects.create(products=product,user=user,quantity=quantity,total=quantity*product.price)
           messages.success(request,'product added sucessfully')
           return redirect('home_view')
        else:
            messages.warning(request,"you must login first!!..")
            return redirect('home_view')
@method_decorator(login_required,name="dispatch")       
class cartlistView(ListView):
    model=Cart
    template_name='cart_list.html'
    context_object_name='product'  
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).exclude(status='order-placed')
        # print(data)
        # price=0
        # for i in data:
        #     price=i.product.price
        #     total=i.quantity*price
        #     print(total)
        #     return {'data':data,'total':total}
    
class OrderView(View):
    def get(self,request,*arg,**kwargs):
        form=OrderForm()
        return render(request,'order.html',{'form':form})
    def post(self,request,*arg,**kwargs):
        email=request.POST.get('email')
        address=request.POST.get('address')
        user=request.user
        cart_pro=Cart.objects.get(id=kwargs.get('id'))  
        orders.objects.create(user=user,product=cart_pro,email=email,address=address)
        cart_pro.status='order-placed'
        cart_pro.save()
        send_mail("shop in style","order placed successfully",settings.EMAIL_HOST_USER,[email])  
        messages.success(request,"order place successfully")
        return redirect('list_view')
@method_decorator(login_required,name="dispatch")
class DemoClass(View):
    def get(self,request):
        return redirect('home_view')