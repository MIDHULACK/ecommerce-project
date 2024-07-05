from ecommerce_app.models import Cart
def cart_count(request):
    user=request.user
    if user.is_authenticated:
        count=Cart.objects.filter(user=user).exclude(status='order-placed').count()
        return{'count':count}
    else:
        return{'count':0}

def total_price(request):
    if request.user.is_authenticated:
        data=Cart.objects.filter(user=request.user).exclude(status='order-placed')  
        price=0
        total=0
        for i in data:
            price=i.products.price
            total=i.quantity*price
            print(total)
            return{'total':total} 