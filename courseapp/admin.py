from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']
    list_filter = ['id','name','created_date']
    search_fields = ['id','name','created_date']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']
    list_filter = ['id','name','created_date']
    search_fields = ['id','name','created_date']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date']
    list_filter = ['id','name','created_date']
    search_fields = ['id','name','created_date']



admin.site.register(Subject_Catagory)