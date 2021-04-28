from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def home(request):
    return render(request, 'shopping/home.html')

@login_required
def products(request):
    products = Products.objects.all()
    return render(request, 'shopping/products.html', {'products':products})

@login_required
def location(request):
    return render(request, 'shopping/location.html')

@login_required
def payment(request, id):
    user = User.objects.get(username=request.user.username)
    product = Products.objects.get(id=id)
    mode = request.GET.get('channel')
    print(mode)
    return render(request, 'shopping/payment.html')

@login_required
def payment_success(request):
    # user = User.objects.get(user=request.user)
    # product = Products.objects.get(id=id)
    # mode = 
    # p = Payment
    return render(request, 'shopping/payment-success.html')