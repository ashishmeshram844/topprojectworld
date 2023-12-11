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



class Blog(models.Model):
    heading = models.CharField(max_length=300)
    image = models.ImageField(upload_to="blog_image")
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     # call the compress function
    #     new_image = compress(self.image)
    #     # set self.image to new_image
    #     self.image = new_image
    #     # save
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.heading



class Blog_Detail(models.Model):
    sel_blog = models.OneToOneField(to=Blog,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog_image",blank = True,null = True)
    video = models.FileField(upload_to='Blog_video',blank=True,null=True)
    doc_file = models.FileField(upload_to='blog_doc_file',blank=True,null=True)
    write_blog = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

   

