from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=40) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


class Student_Account(models.Model):
    sel_user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = "student_account_photo",blank = True,null=True)
    fullname = models.CharField(max_length = 100,blank=True)
    optional_email = models.EmailField(max_length = 100,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    optional_mobile = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length = 300,blank=True,null=True)
    country = models.CharField(max_length = 100,blank=True,null=True)
    state = models.CharField(max_length = 100,blank=True,null=True)
    city = models.CharField(max_length = 100,blank=True,null=True)
    zipcode = models.IntegerField(blank=True,null=True)

    forget_password_token = models.CharField(max_length=300,blank=True,null=True)


    # def save(self, *args, **kwargs):
    #     # call the compress function
    #     new_image = compress(self.photo)
    #     # set self.image to new_image
    #     self.photo = new_image
    #     # save
    #     super().save(*args, **kwargs)




    def __str__(self):
        return self.sel_user.username
    