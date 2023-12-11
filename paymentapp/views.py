from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from courseapp .models import *
from .models import *
#rozorpay
#------------------
import razorpay
import json
import numpy as np



url = 'https://api.razorpay.com/v1'
client = razorpay.Client(auth=("rzp_live_w1RJIJNnHcqCdX", "bGeBWlvBemUuT64LKOGA5Rgn"))



@login_required
def pay(request):
    try:
        user = request.user
        if request.method =='POST':

            customer_name = request.POST['customer_name']
            customer_email = request.POST['customer_email']
            customer_mobile= request.POST['customer_mobile']
            pay_amt = request.POST['pay_amt']
            course = request.POST['course_name']
            course_id = request.POST['course_id']
            pay_amt = float(pay_amt)
            print(type(pay_amt))
            pay_amt = pay_amt*100
            print(pay_amt)
            
            # cust = Customer(course= course, customer_name=customer_name,customer_email=customer_email,customer_mobile=customer_mobile,pay_amt=pay_amt)
            # cust.save()

            data = {
                'amount' : pay_amt,
                'currency' : "INR",
                'receipt': str(random.randint(100000,999999)),
                'notes':{
                    'name' : user.username,
                    'payment_for' : course + " " + "project",
                    'course_id' : course_id
                }
            }
            
            order = client.order.create(data=data)
            orderId = order["id"]
            oder_id = orderId
            print("Order id is",orderId)
            client.order.fetch(orderId)

            # cust = Customer.objects.last()
            # print(cust)
            context = {
                # 'cust' : cust,
                'orderId' : orderId,
                'customer_name' : customer_name,
                'customer_email' : customer_email,
                'customer_mobile' : customer_mobile,
                'pay_amt' : pay_amt,
                'course' : course,
                'course_id' : course_id
                

            }
            
            return render(request, 'paymentapp/pay.html',context)
        else:
            return redirect('student_dashboard')

    except:
        return redirect('student_dashboard')







@csrf_exempt
def success(request):
    try:
        user = request.user
        if request.method == 'POST':
            course_id = request.POST['course_id']
            course_name = request.POST['course_name']
            payment_id = request.POST['razorpay_payment_id']
            order_id = request.POST['razorpay_order_id']
            signature_hash = request.POST['razorpay_signature']
            course = request.POST['course_name']
            paid_amount = float(request.POST['paid_amount'])
          
            paid_amount = paid_amount/100

            sel_project = Project.objects.get(id = course_id)

            paid = Purchased_Project(user = user,sel_project = sel_project,payment_id = payment_id,signature_hash = signature_hash,project_name = course_name,paid_amount = paid_amount)
            paid.save()
            #client.payment.capture(payment_id, amount)
            
            data = client.payment.fetch(payment_id)
            context = {
                'payment_id' : payment_id,
                'course' : course,
                'paid_amount' : paid_amount,
                

            }
            return render(request,'paymentapp/pay_success.html',context)
        else:
            return HttpResponse('<script>window.history.back();</script>')   
        
    except:
        return HttpResponse('<script>window.history.back();</script>')    




