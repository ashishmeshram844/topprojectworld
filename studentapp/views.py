from paymentapp.models import Purchased_Project
from accountapp.models import Student_Account
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import uuid
from django.core.checks.messages import Info
from django.http.response import JsonResponse
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from projectapp .models import *
from .models import *
# Create your views here.


def student_base(request):
    return render(request,'studentapp/student_base.html')



@login_required
def student_dashboard(request):
    user = request.user
    try:
        book = Boorkmark.objects.filter(user= user)
        context = {
            'book' : book
        }
        return render(request,'studentapp/student_dashboard.html',context)
    except:
        return redirect('error_page')


@login_required
def student_profile(request):
    try:
        return render(request,'studentapp/student_profile.html')
    except:
        return redirect('error_page')




@login_required
def edit_student_profile(request):
    try:
        if request.method == "POST":
            user = request.user
            student_profile = Student_Account.objects.get(sel_user = user)
            student_profile.fullname = request.POST['fullname']
            try:
                student_profile.optional_email = request.POST["optional_email"]
            except:
                pass
            student_profile.mobile = request.POST["mobile"]
            try:
                student_profile.optional_mobile = request.POST["optional_mobile"]
            except:
                pass
            student_profile.address = request.POST["address"]
            student_profile.country = request.POST["country"]
            student_profile.state = request.POST["state"]
            student_profile.city = request.POST["city"]
            student_profile.zipcode = request.POST["zipcode"]
            student_profile.save()
            messages.success(request,"Profile Updated Successfully")

        else:
            pass
        return render(request,'studentapp/edit_student_profile.html')
    except:
        return redirect('error_page')



@login_required
def profile_pic_upload(request):
    try:
        if request.method == "POST":
            user = request.user
            stu = Student_Account.objects.get(sel_user = user)
        
            photo = request.FILES['photo']
            stu.photo = photo
            stu.save()
            return redirect('student_dashboard')
    except:
        return redirect('error_page')        


@login_required
def student_purchased_project(request):
    try:
        user = request.user
        pur_project = Purchased_Project.objects.filter(user = user)
        context = {
            'pur_project' : pur_project
        }
        return render(request,'studentapp/student_purchased_project.html',context)  
    except:
        return redirect('error_page')




@login_required
def student_bookmarks(request):
    user = request.user
    try:
        book = Boorkmark.objects.filter(user = user)
        context = {
            'book' : book
        }
        return render(request,'studentapp/student_bookmarks.html',context)
    except:
        return redirect('error_page')



@login_required
def change_student_password(request):
    try:
        user = request.user
        if request.method == "POST":
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            confirm_new_password = request.POST['confirm_new_password']
            if user.check_password(old_password):
                if new_password == confirm_new_password:
                    user.set_password(new_password)
                    user.save()
                    if user is not None:
                        auth.login(request,user)
                    messages.success(request,"Password Changes Successfully ! ")
                else:
                    messages.info(request,"Password not matching ! ")
            else:
                messages.error(request,"Old Password is not correctt ! ")
        else:
            pass
        return render(request,'studentapp/change_student_password.html')
    except:
        return redirect('error_page')


@login_required
def add_new_bookmark(request):
    try:
        user = request.user
        if request.method == "POST":
            name = request.POST['name']
            link = request.POST['link']

            book = Boorkmark(user = user,name = name,link=link)
            book.save()
            messages.success(request,'Bookmark saved successfully')
        else:
            pass
        return redirect('student_bookmarks')
    except:
        return redirect('error_page')




@login_required
def delete_bookmark(request,myid):
    try:
        book = Boorkmark.objects.get(id = myid)
        book.delete()
        messages.success(request,"Bookmarks deleted successfully")
        return redirect('student_bookmarks')
    except:
        return redirect('error_page')



@login_required
def purchased_project_detail(request,myid):
    try:
        user = request.user
        pur_pro = Purchased_Project.objects.get(id = myid)
        pro_id = pur_pro.sel_project.id
        project = Project.objects.get(id = pro_id)
        pp = Purchased_Project.objects.filter(user = user,sel_project = project)
        print("PP : ",pp)
        if pp:
            project_os = Project_Operating_System.objects.filter(sel_project = project)
            project_screens = Project_Screenshot.objects.filter(sel_project = project)
            project_technology = Project_Technology.objects.filter(sel_project = project)
            project_module = Project_Module.objects.filter(sel_project = project)
            project_file = Project_File.objects.filter(sel_project = project)
            context = {
                'project'  : project,
                'pur_pro' : pur_pro,
                'project_os':project_os,
                'project_screens':project_screens,
                'project_technology':project_technology,
                'project_module': project_module,
                'project_file' : project_file
            }
            return render(request,'studentapp/purchased_project_detail.html',context)
        else:
            return redirect('error_page')
    except:
        return redirect('error_page')

        