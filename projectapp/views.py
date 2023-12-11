from django.http.response import HttpResponse
import requests
from accountapp.views import login_page
import projectapp
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required




# @login_required
def Projects(request):
    try:
        projectt = Project.objects.all()
        paginator = Paginator(projectt, 6)
        page_number = request.GET.get('page')
        project = paginator.get_page(page_number)
        context = {
            'project' : project
        }
        return render(request,'projectapp/projects.html',context)
    except:
        return redirect('error_page')
        





def Projects_detail(request,myid):
    try:
        project = Project.objects.get(id = myid)
        project_os = Project_Operating_System.objects.filter(sel_project = project)
        project_screens = Project_Screenshot.objects.filter(sel_project = project)
        project_technology = Project_Technology.objects.filter(sel_project = project)
        project_module = Project_Module.objects.filter(sel_project = project)
        all_projects = Project.objects.all()[:5:-1]
        project_revieww = Project_Review.objects.filter(sel_project = project)[::-1]
        paginator = Paginator(project_revieww, 5)
        page_number = request.GET.get('page')
        project_review = paginator.get_page(page_number)


        context = {
            'project': project,
            'project_os':project_os,
            'project_screens':project_screens,
            'project_technology':project_technology,
            'project_module': project_module,
            'project_review' : project_review,
            'all_projects':all_projects


        }
        return render(request,'projectapp/projects_detail.html',context)
    except:
        return redirect('error_page')




def Projects_filter(request,myid):
    try:
        pro_cat = Project_Catagory.objects.get(id = myid)
        projectt = Project.objects.filter(sel_project_catagory = pro_cat)
        paginator = Paginator(projectt, 8)
        page_number = request.GET.get('page')
        project = paginator.get_page(page_number)
        context = {
            'project':project
        }
        
        return render(request,'projectapp/projects_filter.html',context)
    except:
        return redirect('error_page')



def Search_projects(request):
    try:
        query = request.GET['query']
        context = {}
        if query is not "":
            projectt = Project.objects.filter(name__contains = query)
            paginator = Paginator(projectt,200)
            page_number = request.GET.get('page')
            project = paginator.get_page(page_number)
            context={
                'project': project,
                'query':query
            }

        return render(request,'projectapp/projects_filter.html',context)
    except:
        return redirect('error_page')






def submit_project_review(request):
    try:
        if request.method == "POST":
            id = request.POST['id']
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            project = Project.objects.get(id = id)
            try:
                user = request.user
                project_review = Project_Review(sel_project = project,name=name,email=email,message=message,user=user)
            except:
                project_review = Project_Review(sel_project = project,name=name,email=email,message=message)
            project_review.save()
            print("SUBMIT")
            return redirect('projects_detail',myid=id)
        else:
            pass
    except:
        return redirect('error_page')









def send_project_enquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        enquiry = request.POST['enquiry']
        enq = Project_Enquiry(name=name,email = email,mobile=mobile,enquiry=enquiry)
        enq.save()

    else:
        pass
    return HttpResponse('<script>alert("Enquiry Form submited successfully we will contact you soon");window.history.back();</script>')