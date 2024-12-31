from django.db import models

# Create your models here.

# menu models - product add

from django.db import models
from django.contrib.auth.models import User

# Existing models
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.models import User

# Models
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name


class Items(models.Model):
    Item_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return f"{self.Item_name} - {self.Price}.00rs"


# Cart models
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.item.Price * self.quantity

    def __str__(self):
        return f"{self.item.Item_name} ({self.quantity})"

# custom chatgpt end



# about us

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

# feedback

class Feedback(models.Model):
    User_name = models.CharField(max_length=15, unique=False)
    Description = models.TextField(blank=False, unique=False)
    Rating = models.IntegerField(default=0 , unique=False)
    Image = models.ImageField(upload_to='Items/',blank=True, default='../media/Items/f4.png' )
    Email = models.EmailField(blank=True, unique=False)


    def __str__(self):
        return f"{self.User_name} ({self.Email})"

# boom Table
class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone = models.IntegerField()
    Email = models.EmailField()
    TotalPerson = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return self.Email


# offers model

class Offer(models.Model):
    Day_name = models.CharField(max_length=10)
    Off = models.CharField(max_length=15)
    Image = models.ImageField()


# shipping address

class shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipping_addresses' , null=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.IntegerField(max_length=10)
    address_1 = models.CharField( max_length=50)
    country = models.CharField( max_length=50)
    state = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    zipcode = models.IntegerField( max_length=6)
    

    def __str__(self):
        return f"{self.phone} {self.first_name} {self.country}"


# payment
from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('upi', 'UPI'),
        ('net_banking', 'Net Banking'),
    ])
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.payment_status}"
