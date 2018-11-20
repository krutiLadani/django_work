# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
       product_name = models.CharField(max_length=200)
       product_price = models.IntegerField()
       product_brand = models.CharField(max_length=100)
       product_img = models.ImageField(upload_to='images/')
       product_description = models.CharField(max_length=500)
       def __str__(self):
            return self.product_name


class Cart(models.Model):
    uname = models.ForeignKey(User)
    total_product = models.PositiveIntegerField(default=1)
    product_detail = models.ForeignKey(Product)
    total_price = models.IntegerField(default=0)


class Order(models.Model):
    user_details = models.ForeignKey(User)
    order_amount = models.IntegerField()
    no_of_product = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=13)
    address = models.TextField(max_length=500, blank=True)
    zip = models.CharField(max_length=30,null=True, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30,null=True, blank=True)
   
class Dashboard(models.Model):
    u_items = models.ForeignKey(Order)
    
