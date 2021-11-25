from django.db import models
from products.models import Product
from infores.models import Restaurant
from users.models import User
from django.conf import settings


class Status(models.Model):
    description= models.CharField(max_length=60)
    
    def __str__(self):
        return self.description

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Product, through="ProductDetail")
    def __str__(self):
        return str(self.id)
    


class ProductDetail(models.Model):
    order= models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product+ " Quantity: "+str(quantity)