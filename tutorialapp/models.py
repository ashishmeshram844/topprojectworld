from django.db import models
from django.db.models.base import Model

# Create your models here.
from courseapp .models import *
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.



def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=40) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image



class Tutorial_Detail(models.Model):
    sel_subject = models.ForeignKey(to=Subject,on_delete=models.CASCADE,blank=True,null=True)
    sel_topic = models.ForeignKey(to=Topic,on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    extra_description1 = models.TextField(blank=True,null=True)
    extra_description2 = models.TextField(blank=True,null=True)
    note =models.TextField(blank=True,null=True)
    example_code = models.TextField(blank=True,null=True)
    example_explained = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="tutorial_image",blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    # def save(self, *args, **kwargs):
    #     # call the compress function
    #     new_image = compress(self.image)
    #     # set self.image to new_image
    #     self.image = new_image
    #     # save
    #     super().save(*args, **kwargs)
        

    def __str__(self):
        return self.sel_topic.name +  " == > " + self.heading







