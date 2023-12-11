from django.db import models
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



class Student_Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    country = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email 




class Main_Slider(models.Model):
    heading_text = models.CharField(max_length=100)
    heading_color = models.CharField(max_length=50)
    description = models.TextField()
    description_color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="homepage_slider_images")


    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)



    def __str__(self):
        return self.heading_text



class Homepage_Discover_More_Link(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to="discover_more_images")
    url = models.CharField(max_length=150)


    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.heading





class About_Us_Items(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="about_us_items_logo")

    def __str__(self):
        return self.heading



class Contact_Us_Page(models.Model):
    address1 = models.TextField()
    address2 = models.TextField(blank=True,null=True)
    mobile1 = models.CharField(max_length=20,blank=True,null=True)
    mobile2 = models.CharField(max_length=20,blank=True,null=True)
    mobile3 = models.CharField(max_length=20,blank=True,null=True)
    website1 = models.CharField(max_length=100,blank=True,null=True)
    website2 = models.CharField(max_length=100,blank=True,null=True)
    website3 = models.CharField(max_length=100,blank=True,null=True)

    def __self__(self):
        return self.address1
















