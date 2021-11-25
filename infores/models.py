from django.db import models
from location_field.models.plain import PlainLocationField

class Direction(models.Model):
    city = models.CharField(max_length=100)
    pc = models.CharField(max_length=20)
    street = models.CharField(max_length=60)
    int_number = models.IntegerField()
    ext_number = models.IntegerField()
    state = models.CharField(max_length=100)
    location = PlainLocationField( based_fields=['city'], zoom=7)

    def __str__(self):
        return self.state+' '+self.city+' '+self.pc+' '+self.street+' '+str(self.ext_number)+' '+str(self.int_number)+' '+self.state+' '+self.location

class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    schedule_open = models.TimeField(auto_now=False, auto_now_add=False)
    schedule_close = models.TimeField(auto_now=False, auto_now_add=False)
    direction = models.ForeignKey(Direction, on_delete=models.DO_NOTHING)
    phone_number= models.CharField(max_length=15)
    retaurant_type= models.CharField(max_length=100)

    def __str__(self):
        return self.name