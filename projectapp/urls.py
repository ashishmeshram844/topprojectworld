from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   
    path('projects',views.Projects,name='projects'),
    path('projects_detail/<int:myid>/',views.Projects_detail,name='projects_detail'),
    path('projects_filter/<int:myid>/',views.Projects_filter,name='projects_filter'),
    path('search_projects',views.Search_projects,name='search_projects'),
    path('submit_project_review',views.submit_project_review,name='submit_project_review'),



    path('send_project_enquiry',views.send_project_enquiry,name='send_project_enquiry'),
    
    

]