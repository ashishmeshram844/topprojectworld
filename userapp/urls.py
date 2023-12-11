from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('base',views.Base,name='base'),
    path('',views.Index,name='index'),
    path('about',views.About,name='about'),
    path('contact_us',views.Contact_us,name='contact_us'),
    path('error_page',views.error_page,name='error_page'),
    

   

]