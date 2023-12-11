from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Boorkmark(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
