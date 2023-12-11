
from django.contrib import messages
from django.db import models
from django.shortcuts import render,redirect
from projectapp .models import Project_Catagory
from courseapp .models import Chapter, Subject, Subject_Catagory
from .models import *
from adminapp .models import *
# Create your views here.




def common(request):
    try:
        project_catagory = Project_Catagory.objects.all()
        subject_catagory = Subject_Catagory.objects.all()
        subject = Subject.objects.all()
        chapter = Chapter.objects.all()
        keyward = Keywards.objects.all().last()

        context = {
            'project_catagory':project_catagory,
            'subject_catagory' : subject_catagory,
            'subject' : subject,
            'chapter' : chapter,
            'keyward' : keyward

        }
        return context
    except:
        return redirect('error_page')



def Base(request):
    return render(request,'userapp/base.html')




def Index(request):
   
        slider = Main_Slider.objects.all()
        discover_link = Homepage_Discover_More_Link.objects.all()

        context = {
            'slider' : slider,
            'discover_link' : discover_link
        }
        return render(request,'userapp/index.html',context)




def About(request):
    try:
        about = About_Us_Items.objects.all()
        context = {
            'about' : about
        }
        return render(request,'userapp/about.html',context)
    except:
        return redirect('error_page')




def Contact_us(request):
    cont = Contact_Us_Page.objects.all().last()
    context = {
        'cont' :cont
    }
    try:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            country = request.POST['country']
            message = request.POST['message']
            student_enq = Student_Enquiry(name = name,email = email,mobile=mobile,country=country,message=message)
            student_enq.save()
            messages.success(request,"Your Enquiry Submited Successfully!")

        else:
            pass
        return render(request,'userapp/contact_us.html',context)

    except:
        return redirect('error_page')




def error_page(request):
    return render(request,'error_page.html')