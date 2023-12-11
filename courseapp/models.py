from django.db import models

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


class Subject_Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Subject(models.Model):
    sel_subject_catagory = models.ForeignKey(to=Subject_Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField(upload_to='subject_thumnail')
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    # def save(self, *args, **kwargs):
    #     # call the compress function
    #     new_image = compress(self.thumnail)
    #     # set self.image to new_image
    #     self.thumnail = new_image
    #     # save
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.name



class Chapter(models.Model):
    sel_subject = models.ForeignKey(to=Subject,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thumnail = models.ImageField(upload_to='chapter_thumnail')
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     # call the compress function
    #     new_image = compress(self.thumnail)
    #     # set self.image to new_image
    #     self.thumnail = new_image
    #     # save
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.name


class Topic(models.Model):
    sel_subject = models.ForeignKey(to=Subject,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=150)
    thumnail = models.ImageField(upload_to='chapter_thumnail')
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     # call the compress function
    #     new_image = compress(self.thumnail)
    #     # set self.image to new_image
    #     self.thumnail = new_image
    #     # save
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.name