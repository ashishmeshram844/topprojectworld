from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   
    path('blogs',views.Blogs,name='blogs'),
    path('blogs_detail/<int:myid>/',views.Blogs_detail,name='blogs_detail'),

]