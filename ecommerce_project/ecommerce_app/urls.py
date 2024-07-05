"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from ecommerce_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home.as_view(),name='home_view'),
    path('reg',views.RegisterView.as_view(),name='register_view'),
    path('log',views.LoginView.as_view(),name='login_view'),
    path('logout',views.LogoutView.as_view(),name='logout_view'),
    path('detail/<int:id>', views.Productdetail.as_view(),name='detail_view'),
    path('cart/<int:id>', views.AddCartView.as_view(),name='cart_view'),
    path('cartlist', views.cartlistView.as_view(),name='list_view'),
    path('order/<int:id>', views.OrderView.as_view(),name='order_view'),
    path('demo', views.DemoClass.as_view(),name='demo_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    

