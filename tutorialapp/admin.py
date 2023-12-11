from tutorialapp.models import Tutorial_Detail
from django.contrib import admin
from courseapp .models import *
# Register your models here.





@admin.register(Tutorial_Detail)
class tutorial_DetailAdmin(admin.ModelAdmin):
    list_display = ['id','heading','created_date']
    list_filter = ['id','heading','created_date']
    search_fields = ['id','heading','created_date']

