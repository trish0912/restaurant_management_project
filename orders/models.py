from django.db import models
from .models import Menu
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = [
        ('pending','Pending'),
        ('in_process','In_process'),
        ('completed','Completed')
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", help_text='The customer who placed the order.')
    order_items = models.ManyToManyField(Menu, on_delete=models.CASCADE, related_name="orders", help_text='Menu items included in the order.')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Total amount of the order.')
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending', help_text='Status of the order.')

    # String representation of the Order model
    def __str__(self):
        return f"Order {self.id} by {self.customer.username} - {self.order_status}"