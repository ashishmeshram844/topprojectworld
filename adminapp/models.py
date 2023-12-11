from django.db import models

# Create your models here.


class Keywards(models.Model):
    keyward =  models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
