from enum import auto
from django.db import models
from django.contrib.auth.models import User

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


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Operating_System(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Project_Catagory(models.Model):
    name = models.CharField(max_length=100)
    thumnail = models.ImageField(upload_to="Project_catagory_thumnail",blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.thumnail)
        # set self.image to new_image
        self.thumnail = new_image
        # save
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





class Project(models.Model):
    sel_project_catagory = models.ForeignKey(to=Project_Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    thumnail = models.ImageField(upload_to="project")
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project_Detail(models.Model):
    sel_project = models.OneToOneField(to=Project,on_delete=models.CASCADE)
    database = models.CharField(max_length=100)
    project_title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    offer_price = models.IntegerField()
    helpline_number = models.IntegerField()
    note = models.CharField(max_length=200)
    synopsys = models.FileField(upload_to="project_synopsys",blank=True,null=True)
    report = models.FileField(upload_to="project_reports",blank=True,null=True)
    thesis = models.FileField(upload_to="project_thesis",blank=True,null=True)
    presentation = models.FileField(upload_to="project_presentation",blank=True,null=True)
    project_setup_video = models.FileField(upload_to="project_setup_video",blank=True,null=True)
    project_overview_video = models.FileField(upload_to="project_overview_video",blank=True,null=True)
    project_requirement_file = models.FileField(upload_to="project_requirement_file",blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sel_project.name



class Project_Module(models.Model):
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="project_module_image")
    created_date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sel_project.name





class Project_File(models.Model):
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    zip_file = models.FileField(upload_to='project_zip_files')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sel_project.name





class Project_Screenshot(models.Model):
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="project_screenshot")
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # call the compress function
        new_image = compress(self.image)
        # set self.image to new_image
        self.image = new_image
        # save
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.sel_project.name




class Project_Technology(models.Model):
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    sel_technology = models.ForeignKey(to=Technology,on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sel_project.name





class Project_Operating_System(models.Model):
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    sel_operating_system = models.ForeignKey(to=Operating_System,on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sel_project.name




class Project_Review(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,blank=True,null=True)
    sel_project = models.ForeignKey(to=Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.email






class Project_Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    enquiry = models.TextField()
    created_date = models.DateField(auto_now_add=True,blank=True,null=True)
    
