from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('practice_problems/<int:myid>/',views.Practice_problems,name='practice_problems'),
    path('practice_list',views.Practice_list,name='practice_list'),

    path('program_data/<int:subid>/<int:myid>',views.Program_data,name='program_data'),


]