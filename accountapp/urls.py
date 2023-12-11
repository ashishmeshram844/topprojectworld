from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('forget_password',views.forget_password,name='forget_password'),
    path('opt_confirmation',views.opt_confirmation,name='opt_confirmation'),

    path('change_password',views.change_password,name='change_password'),



    path('login_page',views.login_page,name='login_page'),
    


]