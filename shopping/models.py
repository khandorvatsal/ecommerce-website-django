from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    size = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='Product_pics', default='default.jpg')

    def __str__(self):
        return f'{self.name} : {self.price}'

class Payment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    payment_choice = (('COD', 'COD'), 
                       ('Credit Card', 'Credit Card'))
    payment_type = models.CharField(choices = payment_choice, default='', max_length=30)

    def __str__(self):
        return f'{self.product} : {self.user} : {self.payment_type}'