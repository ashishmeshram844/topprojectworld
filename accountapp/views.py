import requests
from requests.api import request
from accountapp.models import Student_Account
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import uuid
from django.core.checks.messages import Info
from django.http.response import JsonResponse
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from .models import *
from .mail_sender import send_forget_password_mail

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from functools import wraps



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'




def register(request):
    try:
        if is_ajax(request=request) and request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            pass1 = request.POST["pass1"]
            pass2 = request.POST["pass2"]

            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    return JsonResponse({"error": 'Email is Already Registered'}, status=400)
                    
                if User.objects.filter(username = username).exists():
                    return JsonResponse({"error": 'Username is Already Used'}, status=400)
                else:
                    user = User.objects.create_user(username = username,email=email,password=pass1)
                    user.save()
                    student = Student_Account(sel_user = user)
                    student.save()
                    if user is not None:
                        #log in registered user
                        auth.login(request,user)
                        return JsonResponse({"instance": 'success'}, status=200)


                # return JsonResponse({"instance": 'success'}, status=200)
            else:
                return JsonResponse({"error": 'Both Password are not matching'}, status=400)
        else:
            # some error occured
            return JsonResponse({"error": ""}, status=400)
    except:
        return redirect('error_page')





@login_required
def logout(request):
    auth.logout(request)
    return redirect("index")




def login(request):
    try:
        if is_ajax(request=request) and request.method == "POST":
            username = request.POST["username"]
            password = request.POST['password']
            user=auth.authenticate(username = username, password=password)
            if user is not None:
                auth.login(request,user)
                return JsonResponse({"instance": 'success'}, status=200)
            else:
                return JsonResponse({"error": "Invalid Credentials"}, status=400)
        else:
            return JsonResponse({"error": "Invalid Credentials"}, status=400)
    except Exception as e:
        print(e)
        return redirect('error_page')



def forget_password(request):
    try:
        if is_ajax(request=request) and request.method == "POST":
            email = request.POST['forget_pass_email']
            if User.objects.filter(email=email).exists():
                #sent mail code
                user_obj = User.objects.get(email=email)
                token = random.randint(100000,999999)
                student_obj = Student_Account.objects.get(sel_user = user_obj)
                student_obj.forget_password_token = token
                student_obj.save()
                send_forget_password_mail(user_obj.email,token)

                #end send mail logic
                return JsonResponse({"msg": 'OTP sent to Your Mail ID'}, status=200)
            else:
                return JsonResponse({"error": "Please Enter Valid Email Id"}, status=400)

        else:
            return JsonResponse({"error": "Something Went wrong"}, status=400)
    except:
        return redirect('error_page')





def opt_confirmation(request):
    try:
        if is_ajax(request=request) and request.method == "POST":
            otp = request.POST['otp']
            print("OTP : ",otp)
            try:
                student_account = Student_Account.objects.get(forget_password_token = otp)
                print(student_account.sel_user.username)
                return JsonResponse({"msg": student_account.sel_user.username}, status=200)
            except:
                return JsonResponse({"error": "OTP is Invalid"}, status=400)
        else:
            return JsonResponse({"error": "Something went wrong"}, status=400)
    except:
        return redirect('error_page')




def change_password(request):
    try:
        if is_ajax(request=request) and request.method == "POST":
            username = request.POST['change_pass_username']
            pass1 = request.POST['password']
            pass2 = request.POST['confirm_password']
            if User.objects.filter(username=username).exists():
                if pass1 == pass2:
                    user_obj = User.objects.get(username = username)
                    user_obj.set_password(pass1)
                    user_obj.save()
                    stu = Student_Account.objects.get(sel_user = user_obj)
                    stu.forget_password_token = ""
                    stu.save()
                    
                    return JsonResponse({"msg": 'Password Changed Successfully Log In Now '}, status=200)
                    #here update password of user
                    pass
                else:
                    return JsonResponse({"error": "Confirm Password is not Same"}, status=400)
            else:
                return JsonResponse({"error": "User Not Found"}, status=400)
        else:
            return JsonResponse({"error": "Something went wrong"}, status=400)
    except:
        return redirect('error_page')



def login_page(request):
    x = request.get_full_path()
    print(x)
    return HttpResponse('<script>alert("login first");window.history.back();</script>')




