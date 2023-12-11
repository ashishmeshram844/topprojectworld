from django.contrib import admin
from .models import *
# Register your models here.




@admin.register(Project_Catagory)
class Project_catagoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']
    list_filter = ['id','name','created_date']
    search_fields = ['id','name','created_date']







@admin.register(Project)
class PrrojectAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']
    list_filter = ['id','name','created_date']
    search_fields = ['id','name','created_date']






@admin.register(Project_Screenshot)
class Prroject_ScreenshotAdmin(admin.ModelAdmin):
    list_display = ['id','sel_project','name','created_date']
    list_filter = ['id','sel_project','name','created_date']
    search_fields = ['id','sel_project','name','created_date']





@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']




@admin.register(Operating_System)
class Operating_SystemAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']





@admin.register(Project_Technology)
class Prroject_TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id','sel_project','sel_technology','created_date']





@admin.register(Project_Operating_System)
class Prroject_Operating_SystemAdmin(admin.ModelAdmin):
    list_display = ['id','sel_project','sel_operating_system','created_date']





@admin.register(Project_Detail)
class Prroject_DetailAdmin(admin.ModelAdmin):
    list_display = ['id','sel_project','created_date']




@admin.register(Project_File)
class Prroject_FileAdmin(admin.ModelAdmin):
    list_display = ['id','sel_project','created_date']
    


@admin.register(Project_Module)
class Prroject_ModuleAdmin(admin.ModelAdmin):
    list_display = ['id','sel_project','name','created_date']




@admin.register(Project_Review)
class Prroject_ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','email','name','created_date']