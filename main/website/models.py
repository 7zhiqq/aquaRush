from django.db import models
from datetime import date, time
from django.utils import timezone
from django.contrib.auth.models import User

ORDER_STATUS_CHOICES = [
    ('Pending', 'Pending'),              
    ('Out for Delivery', 'Out for Delivery'),  
    ('Delivered', 'Delivered'),           
]

class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    customer_name = models.CharField(max_length=100)
    shipping_address = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=15)
    quantity = models.IntegerField()
    delivery_datetime = models.DateTimeField(default=timezone.now)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)    
    amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        return f"Order {self.order_number} for {self.customer_name}"
