from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('tutorial_languages',views.Tutorial_languages,name='tutorial_languages'),

    path('tutorial_select_language/<int:myid>/',views.Tutorial_select_language,name='tutorial_select_language'),

    path('explore_topic/<int:subid>/<int:myid>/',views.Explore_topic,name='explore_topic'),


    
]