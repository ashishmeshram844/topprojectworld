from django.db import models
from courseapp .models import *

# Create your models here.
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


class Practice_program(models.Model):
    sel_subject = models.ForeignKey(to=Subject,on_delete=models.CASCADE)
    heading = models.CharField(max_length=150)
    image = models.ImageField(upload_to="practice_program_image",blank=True,null=True)
    program = models.TextField()
    note = models.CharField(max_length=100,blank=True,null=True)


    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)


    def __str__(self):
        return self.heading