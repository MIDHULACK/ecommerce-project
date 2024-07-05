from django.contrib import admin
from ecommerce_app.models import Category,Products,Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Cart)