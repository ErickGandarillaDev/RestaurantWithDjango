from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    image = models.TextField()
    def __str__(self):
        return self.name