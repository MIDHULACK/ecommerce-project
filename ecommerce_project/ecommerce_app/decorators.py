from django.contrib import messages
from django.shortcuts import redirect

def login_required(fn):
    def wrapper(request,*arg,**kwargs):
        if not request.user.is_authenticated:
            messages.warning(request,"you must login first")
            return redirect('login_view')
        else:
            return fn(request,*arg,**kwargs)
    return wrapper    