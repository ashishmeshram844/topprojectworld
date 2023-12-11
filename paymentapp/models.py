from projectapp.models import Project
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Purchased_Project(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=300)
    paid_amount = models.FloatField()
    payment_id = models.CharField(max_length=300)
    signature_hash = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

