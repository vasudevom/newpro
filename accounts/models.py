#p2c-21-105

from django.db import models
from django.contrib.auth.models import User
class Extende_user(models.Model):
    phone_number = models.CharField(max_length=10)
    college= models.CharField(max_length=50)
    user=  models.OneToOneField(User,on_delete=models.CASCADE)







# Create your models here.


# Create your models here.
