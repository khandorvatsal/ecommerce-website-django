from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shopping-home'),
    path('products/', views.products, name='products'),
    path('products/payment/<int:id>/', views.payment, name='payment'),
    path('products/payment/success/', views.payment_success, name='payment-success'),
    path('location/', views.location, name='location')
]