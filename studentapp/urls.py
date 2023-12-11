from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('student_base',views.student_base,name="student_base"),
    path('student_dashboard',views.student_dashboard,name="student_dashboard"),
    path('student_profile',views.student_profile,name="student_profile"),
    path('edit_student_profile',views.edit_student_profile,name="edit_student_profile"),

    path('profile_pic_upload',views.profile_pic_upload,name="profile_pic_upload"),

    path('student_purchased_project',views.student_purchased_project,name="student_purchased_project"),

    path('student_bookmarks',views.student_bookmarks,name="student_bookmarks"),
    path('change_student_password',views.change_student_password,name="change_student_password"),

     path('add_new_bookmark',views.add_new_bookmark,name="add_new_bookmark"),

    path('delete_bookmark/<int:myid>/',views.delete_bookmark,name="delete_bookmark"),

    path('purchased_project_detail/<int:myid>/',views.purchased_project_detail,name="purchased_project_detail"),

]