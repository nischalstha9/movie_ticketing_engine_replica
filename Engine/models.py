from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.user.username
    
    

class seat(models.Model):
    seat_no = models.PositiveIntegerField(unique=True)
    order = models.ForeignKey(Order,null=True,blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"Seat No: {self.seat_no}"
    