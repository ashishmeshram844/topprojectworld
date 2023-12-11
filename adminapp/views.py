from adminapp.models import Keywards
from blogapp.models import Blog, Blog_Detail
from django.contrib.auth.decorators import login_required
from tutorialapp.models import Tutorial_Detail
from django.db import reset_queries
from practiceapp.models import Practice_program
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from accountapp .models import *
from django.contrib import messages
from projectapp .models import *
from courseapp .models import *
from django.http import JsonResponse, response
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from userapp .models import *
import json
from studentapp .models import *
from paymentapp .models import *
# Create your views here.





def admin_base(request):
    return render(request,'adminapp/admin_base.html')



@login_required
def admin_home(request):
    if request.user.is_staff:
        return render(request,'adminapp/admin_home.html')
    else:
        return redirect('admin-login')


@login_required
def add_new_user(request):
    if request.user.is_staff:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(email=email).exists():
                messages.success(request,"Email is Already Registered")

            elif User.objects.filter(username = username).exists():
                messages.success(request,"Username Already Taken")
            else:
                usr = User.objects.create_user(username=username,email=email,password=password)
                usr.save()
                stu = Student_Account(sel_user=usr)
                stu.save()
                messages.success(request,"User Created Successfully")

        else:
            pass
        return render(request,'adminapp/add_new_user.html')
    else:
        return redirect('admin-login')



@login_required
def users_list(request):
    if request.user.is_staff:
        student_list = Student_Account.objects.all()
        context = {
            'student_list' : student_list
        }
        return render(request,'adminapp/users_list.html',context)
    else:
        return redirect('admin-login')




@login_required
def delete_user(request,myid):
    if request.user.is_staff:
        usr = User.objects.get(id = myid)
        usr.delete()
        messages.info(request,"User Deleted Successfully")
        return redirect('users_list')
    else:
        return redirect('admin-login')





@login_required
def block_user(request,myid):
    if request.user.is_staff:
        usr = User.objects.get(id = myid)
        usr.is_active = False
        usr.save()
        messages.info(request,"Selected User is Bloked Successfully")
        return redirect('users_list')
    else:
        return redirect('admin-login')




@login_required
def unblock_user(request,myid):
    if request.user.is_staff:
        usr = User.objects.get(id = myid)
        usr.is_active = True
        usr.save()
        messages.info(request,"Selected User is Unblocked Successfully")
        return redirect('users_list')
    else:
        return redirect('admin-login')




@login_required
def view_user(request,myid):
    if request.user.is_staff:
        stu = Student_Account.objects.get(id = myid)
        context = {
            'stu' : stu
        }
        return render(request,'adminapp/add_new_user.html',context)
    else:
        return redirect('admin-login')




def user_bookmark_list(request):
    if request.user.is_staff:
        book = Boorkmark.objects.all()
        context = {
            'book' : book
        }
        return render(request,'adminapp/user_bookmark_list.html',context)
    else:
        return redirect('admin-login')





@login_required
def add_project_catagory(request):
    if request.user.is_staff:
        if request.method == "POST":
            name = request.POST['name']
            thumnail = request.FILES['thumnail']
            description = request.POST['description']
            pro_cat = Project_Catagory(name = name,thumnail = thumnail,description = description)
            pro_cat.save()
            messages.success(request,"Project Catagory Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/add_project_catagory.html')
    else:
        return redirect('admin-login')


@login_required
def project_catagory_list(request):
    if request.user.is_staff:
        pro_cat = Project_Catagory.objects.all()
        context = {
            'pro_cat' : pro_cat
        }
        return render(request,'adminapp/project_catagory_list.html',context)
    else:
        return redirect('admin-login')







@login_required
def delete_project_catagory(request,myid):
    if request.user.is_staff:
        pro_cat = Project_Catagory.objects.get(id = myid)
        pro_cat.delete()
        messages.success(request,"Project Catagory Deleted Successfully")
        return redirect('project_catagory_list')

    else:
        return redirect('admin-login')



@login_required
def view_project_catagory(request,myid):
    if request.user.is_staff:
        pro_cat = Project_Catagory.objects.get(id = myid)
        context = {
            'pro_cat' : pro_cat
        }
        return render(request,'adminapp/add_project_catagory.html',context)
    else:
        return redirect('admin-login')



@login_required
def update_project_catagory(request,myid):
    if request.user.is_staff:
        pro_cat = Project_Catagory.objects.get(id = myid)
        pro_cat.name = request.POST['name']
        pro_cat.description = request.POST['description']
        try:
            pro_cat.thumnail = request.FILES['thumnail']
        except:
            pass
        pro_cat.save()
        messages.success(request,"Project Catagory Updated Successfully")
        context = {
            'pro_cat' : pro_cat
        }
        return render(request,'adminapp/add_project_catagory.html',context)
    else:
        return redirect('admin-login')



@login_required
def add_technology(request):
    if request.user.is_staff:
        if request.method == "POST":
            name = request.POST['name']
            description = request.POST['description']
            tech = Technology(name=name,description=description)
            tech.save()
            messages.success(request,"Technology Addedd Successfully")
        else:
            pass
        return render(request,"adminapp/add_technology.html")
    else:
        return redirect('admin-login')



@login_required
def technology_list(request):
    if request.user.is_staff:
        technology = Technology.objects.all()
        context = {
            'technology' : technology
        }
        return render(request,'adminapp/technology_list.html',context)
    else:
        return redirect('admin-login')





@login_required
def delete_technology(request,myid):
    if request.user.is_staff:
        tech = Technology.objects.get(id = myid)
        tech.delete()
        messages.success(request,"Technology Deleted Successfully")
        return redirect('technology_list')
    else:
        return redirect('admin-login')





@login_required
def view_technology(request,myid):
    if request.user.is_staff:
        tech = Technology.objects.get(id = myid)
        context = {
            'technology' : tech
        }
        return render(request,"adminapp/add_technology.html",context)
    else:
        return redirect('admin-login')





@login_required
def update_technology(request,myid):
    if request.user.is_staff:
        tech = Technology.objects.get(id = myid)
        tech.name = request.POST['name']
        tech.description = request.POST['description']
        tech.save()
        messages.success(request,"Technology Updated Successfully")
        context = {
            'technology' : tech
        }
        return render(request,"adminapp/add_technology.html",context)
    else:
        return redirect('admin-login')





@login_required
def add_os(request):
    if request.user.is_staff:
        if request.method == "POST":
            name = request.POST['name']
            description = request.POST['description']
            os = Operating_System(name=name,description=description)
            os.save()
            messages.success(request,"Operating System Addedd Successfully")
        else:
            pass
        return render(request,"adminapp/add_os.html")
    else:
        return redirect('admin-login')





@login_required
def os_list(request):
    if request.user.is_staff:
        os = Operating_System.objects.all()
        context = {
            'os' : os
        }
        return render(request,'adminapp/os_list.html',context)

    else:
        return redirect('admin-login')




@login_required
def delete_os(request,myid):
    if request.user.is_staff:
        os = Operating_System.objects.get(id = myid)
        os.delete()
        messages.success(request,"OS Deleted Successfully")
        return redirect('os_list')
    else:
        return redirect('admin-login')





@login_required
def view_os(request,myid):
    if request.user.is_staff:
        os = Operating_System.objects.get(id = myid)
        context = {
            'os' : os
        }
        return render(request,"adminapp/add_os.html",context)

    else:
        return redirect('admin-login')




@login_required
def update_os(request,myid):
    if request.user.is_staff:
        os = Operating_System.objects.get(id = myid)
        os.name = request.POST['name']
        os.description = request.POST['description']
        os.save()
        messages.success(request,"OS Updated Successfully")
        context = {
            'os' : os
        }
        return render(request,"adminapp/add_os.html",context)

    else:
        return redirect('admin-login')





@login_required
def add_project(request):
    if request.user.is_staff:
        pro_cat = Project_Catagory.objects.all()
        context = {
            'pro_cat' : pro_cat
        }
        if request.method == "POST":
            sel_project_catagory_id = request.POST['sel_project_catagory']
            sel_project_catagory = Project_Catagory.objects.get(id = sel_project_catagory_id)
            name = request.POST['name']
            thumnail = request.FILES['thumnail']
            description = request.POST['description']
            sel_project = Project(sel_project_catagory=sel_project_catagory,name=name,thumnail=thumnail,description=description)
            sel_project.save()

            database = request.POST['database']
            project_title = request.POST['project_title']
            project_type = request.POST['project_type']
            price = int(request.POST['price'])
            discount = int(request.POST['discount'])
            offer_price = price - (price*discount/100)
            helpline_number = request.POST['helpline_number']
            note = request.POST['note']
            synopsys = request.FILES['synopsys']
            project_setup_video = request.FILES['project_setup_video']
            project_overview_video = request.FILES['project_overview_video']
            project_requirement_file = request.FILES['project_requirement_file']
            report = request.FILES['report']
            presentation = request.FILES['presentation']
            
            
            try:
                thesis = request.FILES['thesis']
                pro_detail = Project_Detail(sel_project = sel_project,database=database,project_title=project_title,project_type=project_type,price = price,discount=discount,offer_price=offer_price,helpline_number=helpline_number,note=note,synopsys=synopsys,project_setup_video=project_setup_video,project_overview_video=project_overview_video,project_requirement_file=project_requirement_file,report = report,thesis=thesis,presentation=presentation)
            except:
                pro_detail = Project_Detail(sel_project = sel_project,database=database,project_title=project_title,project_type=project_type,price = price,discount=discount,offer_price=offer_price,helpline_number=helpline_number,note=note,synopsys=synopsys,project_setup_video=project_setup_video,project_overview_video=project_overview_video,project_requirement_file=project_requirement_file,report = report,presentation=presentation)
            pro_detail.save()
            messages.success(request,"Project Added successfully")

        else:
            pass
        return render(request,"adminapp/add_project.html",context)
    else:
        return redirect('admin-login')



@login_required
def project_list(request):
    if request.user.is_staff:
        project = Project_Detail.objects.all()
        context = {
            'project' : project
        }
        return render(request,'adminapp/project_list.html',context)

    else:
        return redirect('admin-login')




@login_required
def delete_project(request,myid):
    if request.user.is_staff:
        project = Project_Detail.objects.get(id = myid)
        project.delete()
        messages.success(request,"Project Deleted Successfully")
        return redirect('project_list')

    else:
        return redirect('admin-login')




@login_required
def view_project(request,myid):
    if request.user.is_staff:
        pro = Project_Detail.objects.get(id = myid)
        pro_cat = Project_Catagory.objects.all()

        context = {
            'pro' : pro,
            'pro_cat' : pro_cat
        }

        return render(request,'adminapp/add_project.html',context)
    else:
        return redirect('admin-login')






@login_required
def update_project(request,myid):
    if request.user.is_staff:
        project_detail = Project_Detail.objects.get(id = myid)
        project = Project.objects.get(id = project_detail.sel_project.id)
        sel_project_catagory = request.POST['sel_project_catagory']
        cat = Project_Catagory.objects.get(id = sel_project_catagory)
        project.sel_project_catagory = cat
        project.name = request.POST['name']
        project.description = request.POST['description']
        project_detail.database = request.POST['database']
        project_detail.project_title = request.POST['project_title']
        project_detail.project_type = request.POST['project_type']
        project_detail.price = int(request.POST['price'])
        project_detail.discount = int(request.POST['discount'])
        offer_price = project_detail.price - (project_detail.price*project_detail.discount/100)
        project_detail.offer_price = offer_price
        project_detail.helpline_number = request.POST['helpline_number']
        project_detail.note = request.POST['note']
        try:
            project_detail.synopsys = request.FILES['synopsys']
        except:
            pass

        try:
            project_detail.report = request.FILES['report']
        except:
            pass

        try:
            project_detail.thesis = request.FILES['thesis']
        except:
            pass

        try:
            project_detail.presentation = request.FILES['presentation']
        except:
            pass

        try:
            project_detail.project_setup_video = request.FILES['project_setup_video']
        except:
            pass

        try:
            project_detail.project_overview_video = request.FILES['project_overview_video']
        except:
            pass

        try:
            project_detail.project_requirement_file = request.FILES['project_requirement_file']
        except:
            pass

        try:
            project.thumnail = request.FILES['thumnail']
        except:
            pass

        project.save()
        project_detail.save()

        messages.success(request,"Project Updated Successfully")
        context = {
            'pro' : project_detail
        }
        return redirect('project_list')
    else:
        return redirect('admin-login')





@login_required
def add_project_technology(request):
    if request.user.is_staff:
        project = Project.objects.all()
        technology = Technology.objects.all()
        context = {
            'project' : project,
            'technology' : technology
        }

        if request.method == "POST":
            project_id = request.POST['sel_project']
            technology_id = request.POST['sel_technology']
        
            description = request.POST['description']
            pro = Project.objects.get(id=project_id)
            techno = Technology.objects.get(id = technology_id)
            pro_technology = Project_Technology(sel_project = pro,sel_technology = techno,description = description)
            pro_technology.save()
            messages.success(request,"Project Technology Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/add_project_technology.html',context)

    else:
        return redirect('admin-login')






@login_required
def project_technology_list(request):
    if request.user.is_staff:
        project_tech = Project_Technology.objects.all()
        context = {
            'project_tech' : project_tech
        }
        return render(request,'adminapp/project_technology_list.html',context)
    else:
        return redirect('admin-login')
        




@login_required
def delete_pro_tech(request,myid):
    if request.user.is_staff:
        pro_tech = Project_Technology.objects.get(id = myid)
        pro_tech.delete()
        messages.success(request,"Project Technology Deleted Successfully")
        return redirect('project_technology_list')
    else:
        return redirect('admin-login')


@login_required
def view_pro_tech(request,myid):
    if request.user.is_staff:
        pro_tech = Project_Technology.objects.get(id = myid)
        project = Project.objects.all()
        technology = Technology.objects.all()
        context = {
            'project' : project,
            'technology' : technology,
            'pro_tech' : pro_tech
        }

        return render(request,'adminapp/add_project_technology.html',context)
    else:
        return redirect('admin-login')





@login_required
def update_pro_tech(request,myid):
    if request.user.is_staff:
        pro_tech = Project_Technology.objects.get(id = myid)
        context = {
            'pro_tech' : pro_tech
        }
        if request.method == "POST":
            project_id = request.POST['sel_project']
            technology_id = request.POST['sel_technology']
            description = request.POST['description']
            pro = Project.objects.get(id = project_id)
            tech = Technology.objects.get(id = technology_id)

            pro_tech.sel_project = pro
            pro_tech.sel_technology = tech
            pro_tech.description = description
            pro_tech.save()
            messages.success(request,"Project Technology Updated SUccessfully")
        else:
            pass
        
        return redirect('project_technology_list')
    else:
        return redirect('admin-login')





@login_required
def add_project_screenshot(request):
    if request.user.is_staff:
        project = Project.objects.all()
        context = {
            'project' : project,
        }

        if request.method == "POST":
            project_id = request.POST['sel_project']
            name = request.POST['name']
            image = request.FILES['image']
            description = request.POST['description']
            pro = Project.objects.get(id = project_id)
            screen = Project_Screenshot(sel_project = pro,name = name,image = image,description = description )
            screen.save()

            messages.success(request,"Project Screenshot  Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/add_project_screenshot.html',context)
    else:
        return redirect('admin-login')






@login_required
def project_screenshot_list(request):
    if request.user.is_staff:
        pro_screen = Project_Screenshot.objects.all()
        context = {
            'pro_screen' : pro_screen
        }
        return render(request,'adminapp/project_screenshot_list.html',context)
    else:
        return redirect('admin-login')



@login_required
def delete_pro_screen(request,myid):
    if request.user.is_staff:
        pro_screen = Project_Screenshot.objects.get(id = myid)
        pro_screen.delete()
        messages.success(request,"Project Screenshot Deleted Successfully")
        return redirect('project_screenshot_list')
    else:
        return redirect('admin-login')



@login_required
def view_pro_screen(request,myid):
    if request.user.is_staff:
        project = Project.objects.all()
        pro_screen = Project_Screenshot.objects.get(id = myid)
        context = {
            'project_screen' : pro_screen,
            'project' : project
        }
        return render(request,'adminapp/add_project_screenshot.html',context)
    else:
        return redirect('admin-login')




@login_required
def update_pro_screen(request,myid):
    if request.user.is_staff:
        if request.method == "POST":
            pro_screen = Project_Screenshot.objects.get(id = myid)
            sel_project_id = request.POST['sel_project']
            sel_project = Project.objects.get(id = sel_project_id)

            pro_screen.sel_project = sel_project
            pro_screen.name = request.POST['name']
            try:
                pro_screen.image = request.FILES['photo']
            except:
                pass
            pro_screen.description = request.POST['description']
            pro_screen.save()
            messages.success(request,"Project ScreenShot Updated SUccessfully")
        else:
            pass

        return redirect('project_screenshot_list')
    else:
        return redirect('admin-login')





@login_required
def add_project_file(request):
    if request.user.is_staff:
        project = Project.objects.all()
        context = {
            'project' : project,
        }

        if request.method == "POST":
            project_id = request.POST['sel_project']
            name = request.POST['name']
            zip_file = request.FILES['zip_file']
            description = request.POST['description']
            pro = Project.objects.get(id = project_id)
            pro_file = Project_File(sel_project = pro,name = name,zip_file = zip_file,description = description )
            pro_file.save()

            messages.success(request,"Project File  Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/add_project_file.html',context)
    else:
        return redirect('admin-login')






@login_required
def project_file_list(request):
    if request.user.is_staff:
        pro_file = Project_File.objects.all()
        context = {
            'pro_file' : pro_file
        }
        return render(request,'adminapp/project_file_list.html',context)

    else:
        return redirect('admin-login')


@login_required
def delete_project_file(request,myid):
    if request.user.is_staff:
        pro_file = Project_File.objects.get(id = myid)
        pro_file.delete()
        messages.success(request,"Project File Deleted Successfully")
        return redirect('project_file_list')
    else:
        return redirect('admin-login')




@login_required
def view_project_file(request,myid):
    if request.user.is_staff:
        project = Project.objects.all()
        pro_file = Project_File.objects.get(id = myid)
        context = {
            'pro_file' : pro_file,
            'project' : project
        }
        return render(request,'adminapp/add_project_file.html',context)
    else:
        return redirect('admin-login')



@login_required
def update_project_file(request,myid):
    if request.user.is_staff:
        pro_file = Project_File.objects.get(id = myid)
        if request.method == "POST":
            sel_pro_id = request.POST['sel_project']
            pro = Project.objects.get(id = sel_pro_id)
            pro_file.sel_project = pro
            pro_file.name = request.POST['name']
            pro_file.description = request.POST['description']
            try:
                pro_file.zip_file = request.FILES['zip_file']
            except:
                pass
            pro_file.save()
            messages.success(request,"Project file Updated successfully")

        else:
            pass
        return redirect('project_file_list')
    else:
        return redirect('admin-login')






@login_required
def add_project_os(request):
    if request.user.is_staff:
        project = Project.objects.all()
        os = Operating_System.objects.all()
        context = {
            'project' : project,
            'os' : os
        }

        if request.method == "POST":
            project_id = request.POST['sel_project']
            os_id = request.POST['sel_operating_system']
            description = request.POST['description']
            pro = Project.objects.get(id = project_id)
            sel_operating_system = Operating_System.objects.get(id = os_id)
            pro_os = Project_Operating_System(sel_project = pro,description = description ,sel_operating_system = sel_operating_system)
            pro_os.save()

            messages.success(request,"Project OS  Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/add_project_os.html',context)
    else:
        return redirect('admin-login')






@login_required
def project_os_list(request):
    if request.user.is_staff:
        pro_os = Project_Operating_System.objects.all()
        context = {
            'pro_os' : pro_os
        }
        return render(request,'adminapp/project_os_list.html',context)
    else:
        return redirect('admin-login')




@login_required
def delete_project_os(request,myid):
    if request.user.is_staff:
        pro_os = Project_Operating_System.objects.get(id = myid)
        pro_os.delete()
        messages.success(request,"Project Operating System Delted successfully")
        return redirect('project_os_list')
    else:
        return redirect('admin-login')






@login_required
def add_project_module(request):
    if request.user.is_staff:
        project = Project.objects.all()
        context = {
            'project' : project,
        }

        if request.method == "POST":
            project_id = request.POST['sel_project']
            name = request.POST['name']
            image = request.FILES['image']
            description = request.POST['description']
            pro = Project.objects.get(id = project_id)
            pro_module = Project_Module(sel_project = pro,description = description,name = name,image = image)
            pro_module.save()

            messages.success(request,"Project Module  Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/add_project_module.html',context)
    else:
        return redirect('admin-login')



@login_required
def project_module_list(request):
    if request.user.is_staff:
        pro_module = Project_Module.objects.all()
        context = {
            'pro_module' : pro_module
        }
        return render(request,'adminapp/project_module_list.html',context)
    else:
        return redirect('admin-login')




@login_required
def delete_project_module(request,myid):
    if request.user.is_staff:
        pro_module = Project_Module.objects.get(id = myid)
        pro_module.delete()
        messages.success(request,"Project Module Delted successfully")
        return redirect('project_module_list')
    else:
        return redirect('admin-login')




@login_required
def view_project_module(request,myid):
    if request.user.is_staff:
        project = Project.objects.all()
        pro_module = Project_Module.objects.get(id = myid)
        context = {
            'pro_module' : pro_module,
            'project' : project
        }
        return render(request,'adminapp/add_project_module.html',context)
    else:
        return redirect('admin-login')




@login_required
def update_project_module(request,myid):
    if request.user.is_staff:
        pro_module = Project_Module.objects.get(id = myid)
        if request.method == "POST":
            sel_project_id = request.POST['sel_project']
            pro = Project.objects.get(id = sel_project_id)
            pro_module.sel_project = pro
            pro_module.name = request.POST['name']
            pro_module.description = request.POST['description']
            try:
                pro_module.image = request.FILES['image']
            except:
                pass
            pro_module.save()
            messages.success(request,"Project Module Updated Successfully")

        else:
            pass

        return redirect('project_module_list')
    else:
        return redirect('admin-login')




@login_required
def project_review_list(request):
    if request.user.is_staff:
        project_review = Project_Review.objects.all()
        context = {
            'project_review' : project_review
        }
        return render(request,"adminapp/project_review_list.html",context)
    else:
        return redirect('admin-login')




@login_required
def delete_project_review(request,myid):
    if request.user.is_staff:
        project_review = Project_Review.objects.get(id = myid)
        project_review.delete()
        messages.success(request,"Project Review deleted successfully")
        return redirect('project_review_list')
    else:
        return redirect('admin-login')




@login_required
def add_subject_catagory(request):
    if request.user.is_staff:
        if request.method == "POST":
            name = request.POST['name']
            description = request.POST['description']
            sub_cat = Subject_Catagory(name = name,description=description)
            sub_cat.save()
            messages.success(request,"Subject Catagory Addedd Successfully")

        else:
            pass
        return render(request,'adminapp/add_subject_catagory.html')
    else:
        return redirect('admin-login')





@login_required
def subject_catagory_list(request):
    if request.user.is_staff:
        sub_cat = Subject_Catagory.objects.all()
        context = {
            'sub_cat' : sub_cat
        }
        return render(request,'adminapp/subject_catagory_list.html',context)
    else:
        return redirect('admin-login')





@login_required
def delete_sub_cat(request,myid):
    if request.user.is_staff:
        sub_cat = Subject_Catagory.objects.get(id = myid)
        sub_cat.delete()
        messages.success(request,"Subject catagory deletedd successfully")
        return redirect('subject_catagory_list')
    else:
        return redirect('admin-login')




@login_required
def view_sub_cat(request,myid):
    if request.user.is_staff:
        sub_cat = Subject_Catagory.objects.get(id = myid)
        context = {
            'sub_cat' : sub_cat
        }
        return render(request,'adminapp/add_subject_catagory.html',context)
    else:
        return redirect('admin-login')



@login_required
def update_sub_cat(request,myid):
    if request.user.is_staff:
        sub_cat = Subject_Catagory.objects.get(id = myid)
        if request.method == "POST":
            sub_cat.name = request.POST['name']
            sub_cat.description = request.POST['description']
            sub_cat.save()
            messages.success(request,"Subject catagory Updated successfully")
        else:
            pass
        return redirect('subject_catagory_list')
    else:
        return redirect('admin-login')






@login_required
def add_subject(request):
    if request.user.is_staff:
        subject_cat = Subject_Catagory.objects.all()
        context = {
            'subject_cat' : subject_cat
        }
        if request.method == "POST":
            sel_subject_catagory_id = request.POST['sel_subject_catagory']
            sel_subject_catagory = Subject_Catagory.objects.get(id = sel_subject_catagory_id)
            name = request.POST['name']
            thumnail = request.FILES['thumnail']
            description = request.POST['description']
            sub = Subject(sel_subject_catagory=sel_subject_catagory,name=name,thumnail=thumnail,description=description)
            sub.save()
            messages.success(request,"Subject Addedd Successfully")

        else:
            pass
        return render(request,'adminapp/add_subject.html',context)
    else:
        return redirect('admin-login')



@login_required
def subject_list(request):
    if request.user.is_staff:
        sub = Subject.objects.all()
        context = {
            'sub' : sub
        }
        return render(request,'adminapp/subject_list.html',context)
    else:
        return redirect('admin-login')



@login_required
def delete_subject(request,myid):
    if request.user.is_staff:
        sub = Subject.objects.get(id = myid)
        sub.delete()
        messages.success(request,"Subjectb Deleted Successfully")
        return redirect('subject_list')
    else:
        return redirect('admin-login')



@login_required
def view_subject(request,myid):
    if request.user.is_staff:
        sub = Subject.objects.get(id = myid)
        subject_cat = Subject_Catagory.objects.all()
        context = {
            'sub' : sub,
            'subject_cat' : subject_cat
        }
        return render(request,'adminapp/add_subject.html',context)
    else:
        return redirect('admin-login')


@login_required
def update_subject(request,myid):
    if request.user.is_staff:
        sub = Subject.objects.get(id = myid)
        context = {
            'sub' : sub
        }
        if request.method == "POST":
            sel_subject_catagory_id = request.POST['sel_subject_catagory']
            sel_subject_catagory = Subject_Catagory.objects.get(id = sel_subject_catagory_id)
            sub.sel_subject_catagory = sel_subject_catagory
            sub.name = request.POST['name']
            try:
                sub.thumnail = request.FILES['thumnail']
            except:
                pass
            sub.description = request.POST['description']
            sub.save()
            messages.success(request,"Subject Updated successfully")

        else:
            pass

        return redirect('subject_list')
    else:
        return redirect('admin-login')




@login_required
def add_program(request):
    if request.user.is_staff:
        sub = Subject.objects.all()
        context = {
            'sub' : sub
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sub = Subject.objects.get(id = sel_subject_id)
            heading = request.POST['heading']
            
            program = request.POST['program']
            note = request.POST['note']
            try:
                image = request.FILES['image']
                prgrm = Practice_program(sel_subject = sub,heading = heading,image = image,program = program,note = note)
            except:
                prgrm = Practice_program(sel_subject = sub,heading = heading,program = program,note = note)
            prgrm.save()
            messages.success(request,"Program Addedd successfully")
        else:
            pass
        return render(request,'adminapp/add_program.html',context)
    else:
        return redirect('admin-login')



@login_required
def program_list(request):
    if request.user.is_staff:
        prgrm_list = Practice_program.objects.all()
        context = {
            'prgrm_list' : prgrm_list
        }
        return render(request,'adminapp/program_list.html',context)
    else:
        return redirect('admin-login')


@login_required  
def delete_program(request,myid):
    if request.user.is_staff:
        prg = Practice_program.objects.get(id = myid)
        prg.delete()
        messages.success(request,"Program Deleted successfully")
        return redirect('program_list')
    else:
        return redirect('admin-login')





@login_required
def view_program(request,myid):
    if request.user.is_staff:
        sub = Subject.objects.all()
        practice_program = Practice_program.objects.get(id = myid)
        context = {
            'practice_program' : practice_program,
            'sub' : sub
        }
        return render(request,'adminapp/add_program.html',context)
    else:
        return redirect('admin-login')




@login_required
def update_program(request,myid):
    if request.user.is_staff:
        practice_program = Practice_program.objects.get(id = myid)
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            practice_program.sel_subject = sel_subject
            practice_program.heading = request.POST['heading']
            try:
                practice_program.image = request.FILES['image']
            except:
                pass
            practice_program.note = request.POST['note']
            practice_program.program = request.POST['program']
            practice_program.save()
            messages.success(request,"Program updated successfully")
            
        else:
            pass

        return redirect('program_list')
    else:
        return redirect('admin-login')






@login_required
def add_chapter(request):
    if request.user.is_staff:
        sub = Subject.objects.all()
        context = {
            'sub' : sub
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            name = request.POST['name']
            thumnail = request.FILES['thumnail']
            description = request.POST['description']

            chapter = Chapter(sel_subject =sel_subject,name=name,thumnail = thumnail,description=description)
            chapter.save()
            messages.success(request,"Chapter Addedd suceessfully")

        else:
            pass

        return render(request,'adminapp/add_chapter.html',context)
    else:
        return redirect('admin-login')



@login_required
def chapter_list(request):
    if request.user.is_staff:
        chapter = Chapter.objects.all()
        context = {
            'chapter' : chapter
        }
        return render(request,'adminapp/chapter_list.html',context)
    else:
        return redirect('admin-login')



@login_required
def delete_chapter(request,myid):
    if request.user.is_staff:
        chapter = Chapter.objects.get(id = myid)
        chapter.delete()
        messages.success(request,"Chapter Deleted Successfully")
        return redirect('chapter_list')
    else:
        return redirect('admin-login')


@login_required
def view_chapter(request,myid):
    if request.user.is_staff:
        chapter_avail = Chapter.objects.get(id = myid)
        sub = Subject.objects.all()
        context = {
            'chapter_avail' : chapter_avail,
            'sub' : sub
        }
        return render(request,'adminapp/add_chapter.html',context)
    else:
        return redirect('admin-login')


@login_required
def update_chapter(request,myid):
    if request.user.is_staff:
        chapter = Chapter.objects.get(id = myid)
        context = {
            'chapter' : chapter
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            chapter.sel_subject = sel_subject
            chapter.name = request.POST['name']
            chapter.description = request.POST['description']
            try:
                chapter.thumnail = request.FILES['thumnail']
            except:
                pass
            chapter.save()
            messages.success(request,"Chapter Updated Successfully")
        else:
            pass
        return redirect('chapter_list')
    else:
        return redirect('admin-login')




@login_required
def add_topic(request):
    if request.user.is_staff:
        sub = Subject.objects.all()
        context = {
            'sub' : sub
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            name = request.POST['name']
            thumnail = request.FILES['thumnail']
            description = request.POST['description']
            topic = Topic(sel_subject = sel_subject,name=name,description=description,thumnail=thumnail)
            topic.save()
            messages.success(request,'Topic Addedd Successfully')
        else:
            pass
        return render(request,'adminapp/add_topic.html',context)
    else:
        return redirect('admin-login')



@login_required
def topic_list(request):
    if request.user.is_staff:
        topic = Topic.objects.all()
        context = {
            'topic' : topic
        }
        return render(request,'adminapp/topic_list.html',context)
    else:
        return redirect('admin-login')


@login_required
def delete_topic(request,myid):
    if request.user.is_staff:
        topic = Topic.objects.get(id = myid)
        topic.delete()
        messages.success(request,"Topic Deleted Successfully")
        return redirect('topic_list')
    else:
        return redirect('admin-login')



@login_required
def view_topic(request,myid):
    if request.user.is_staff:
        sub = Subject.objects.all()
        topic = Topic.objects.get(id = myid)
        context = {
            'sub' : sub,
            'topic' : topic
        }
        return render(request,'adminapp/add_topic.html',context)
    else:
        return redirect('admin-login')





@login_required
def update_topic(request,myid):
    if request.user.is_staff:
        topic = Topic.objects.get(id = myid)
        context = {
            'topic' : topic
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            topic.sel_subject = sel_subject
            topic.name = request.POST['name']
            topic.description = request.POST['description']
            try:
                topic.thumnail = request.FILES['thumnail']
            except:
                pass
            topic.save()
            messages.success(request,"Topic Updated SUccessfully")
        else:
            pass

        return redirect('topic_list')
    else:
        return redirect('admin-login')
        


@login_required
def add_tutorial_detail(request):
    if request.user.is_staff:
        sub = Subject.objects.all()
        topic = Topic.objects.all()
        context = {
            'sub' : sub,
            'topic' : topic
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_topic_id = request.POST['sel_topic']
            heading = request.POST['heading']
            description = request.POST['description']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            seL_topic = Topic.objects.get(id=sel_topic_id)
            tutorial_detail = Tutorial_Detail(sel_subject = sel_subject,sel_topic=seL_topic,heading = heading,description=description)
            tutorial_detail.save()
            messages.success(request,'Tutorial Detail addedd successfully')

        else:
            pass
        return render(request,'adminapp/add_tutorial_detail.html',context)

    else:
        return redirect('admin-login')



@login_required
def tutorial_detail_list(request):
    if request.user.is_staff:
        tutorial_detail = Tutorial_Detail.objects.all()
        context = {
            'tutorial_detail' : tutorial_detail
        }
        return render(request,'adminapp/tutorial_detail_list.html',context)
    else:
        return redirect('admin-login')


@login_required
def delete_tutorial_detail(request,myid):
    if request.user.is_staff:
        tutorial_detail = Tutorial_Detail.objects.get(id = myid)
        tutorial_detail.delete()
        messages.success(request,"Tutorial Detail Deleted Successfully")
        return redirect('tutorial_detail_list')
    else:
        return redirect('admin-login')




@login_required
def view_tutorial_detail(request,myid):
    if request.user.is_staff:
        tutorial_detail = Tutorial_Detail.objects.get(id = myid)
        sub = Subject.objects.all()
        topic = Topic.objects.all()
        context = {
            'sub' : sub,
            'topic' : topic,
            'tutorial_detail':tutorial_detail
        }
        return render(request,'adminapp/add_tutorial_detail.html',context)
    else:
        return redirect('admin-login')


@login_required
def update_tutorial_detail(request,myid):
    if request.user.is_staff:
        tutorial_detail = Tutorial_Detail.objects.get(id=myid)
        context = {
            'tutorial_detail' : tutorial_detail
        }
        if request.method == "POST":
            sel_subject_id = request.POST['sel_subject']
            sel_topic_id = request.POST['sel_topic']
            sel_subject = Subject.objects.get(id = sel_subject_id)
            seL_topic = Topic.objects.get(id=sel_topic_id)

            tutorial_detail.sel_subject = sel_subject
            tutorial_detail.sel_topic = seL_topic
            tutorial_detail.heading = request.POST['heading']
            tutorial_detail.description = request.POST['description']
            try:
                tutorial_detail.extra_description1 = request.POST['extra_description1']
            except:
                pass

            try:
                tutorial_detail.extra_description2 = request.POST['extra_description2']
            except:
                pass

            try:
                tutorial_detail.note = request.POST['note']
            except:
                pass

            try:
                tutorial_detail.example_code = request.POST['example_code']
            except:
                pass

            try:
                tutorial_detail.example_explained = request.POST['example_explained']
            except:
                pass

            try:
                tutorial_detail.image = request.FILES['image']
            except:
                pass

            tutorial_detail.save()

            messages.success(request,"Tutorial Detail Updated Successfully")
        else:
            pass

        return redirect('tutorial_detail_list')
    else:
        return redirect('admin-login')





def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username = username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home')
            else:
                messages.success(request,"Please Enter Valid Credentials")
                return render(request,'adminapp/admin-login.html')
        else:
            messages.success(request,"Invalid Credentials")
            return render(request,'adminapp/admin-login.html')

    else:
        pass
    return render(request,'adminapp/admin-login.html')

    



def admin_logout(request):
    auth.logout(request)
    return redirect('admin-login')



@login_required
def homepage_slider_list(request):
    if request.user.is_staff:
        main_slider = Main_Slider.objects.all()
        context = {
            'main_slider':main_slider
        }
        return render(request,'adminapp/homepage_slider_list.html',context)
    else:
        return redirect('admin-login')



@login_required
def view_homepage_slider(request,myid):
    if request.user.is_staff:
        main_slider = Main_Slider.objects.get(id = myid)
        context = {
            'main_slider' : main_slider
        }
        return render(request,'adminapp/view_homepage_slider.html',context)
    else:
        return redirect('admin-login')



@login_required
def update_home_slider(request,myid):
    if request.user.is_staff:
        main_slider = Main_Slider.objects.get(id = myid)
        context = {
            'main_slider' : main_slider
        }
        if request.method == "POST":
            heading_text = request.POST['heading_text']
            heading_color = request.POST['heading_color']
            description = request.POST['description']
            description_color = request.POST['description_color']
            try:
                image = request.FILES['image']
                main_slider.image = image
            except:
                pass
            main_slider.heading_text  = heading_text
            main_slider.heading_color = heading_color
            main_slider.description = description
            main_slider.description_color = description_color

            main_slider.save()
            messages.success(request,"Slider Updated SUccessfully")

        else:
            pass
        return redirect('homepage_slider_list')

    else:
        return redirect('admin-login')




@login_required
def add_homepage_discover_more(request):
    if request.user.is_staff:
        if request.method == "POST":
            heading = request.POST['heading']
            image = request.FILES['image']
            url = request.POST['url']
            discover_more_links = Homepage_Discover_More_Link(heading=heading,image=image,url=url)
            discover_more_links.save()
            messages.success(request,"Discover more link addedd successfuly")
        else:
            pass
        return render(request,'adminapp/add_homepage_discover_more.html')

    else:
        return redirect('admin-login')


@login_required
def discover_more_list(request):
    if request.user.is_staff:
        discover_more_links = Homepage_Discover_More_Link.objects.all()
        context = {
            'discover_more_links' : discover_more_links
        }
        return render(request,'adminapp/discover_more_list.html',context)
    else:
        return redirect('admin-login')




@login_required
def delete_discover_more_link(request,myid):
    if request.user.is_staff:
        discover = Homepage_Discover_More_Link.objects.get(id= myid)
        discover.delete()
        messages.success(request,'Discover more link deleted successfully')
        return redirect('discover_more_list')
    else:
        return redirect('admin-login')




@login_required
def view_discover_more(request,myid):
    if request.user.is_staff:
        discover = Homepage_Discover_More_Link.objects.get(id= myid)
        context = {
            'discover' : discover
        }
        return render(request,'adminapp/add_homepage_discover_more.html',context)
    else:
        return redirect('admin-login')



@login_required
def update_discover_more_link(request,myid):
    if request.user.is_staff:
        discover = Homepage_Discover_More_Link.objects.get(id= myid)
        context = {
            'discover' : discover
        }
        if request.method == "POST":
            discover.heading = request.POST['heading']
            discover.url = request.POST['url']
            try:
                discover.image = request.FILES['image']
            except:
                pass
            discover.save()
            messages.success(request,"Discover more link updated successfully")
        else:
            pass
        return redirect('discover_more_list')
    else:
        return redirect('admin-login')




@login_required
def contact_us_page(request):
    if request.user.is_staff:
        contact = Contact_Us_Page.objects.all().last()
        context = {
            'contact' : contact
        }
        return render(request,'adminapp/contact_us_page.html',context)
    else:
        return redirect('admin-login')


@login_required
def update_contact_us_page(request,myid):
    if request.user.is_staff:
        contact = Contact_Us_Page.objects.get(id = myid)
        context = {
            'contact' : contact
        }
        if request.method == "POST":
            address1 = request.POST['address1']
            contact.address1 = address1

            try:
                address2 = request.POST['address2']
                contact.address2 = address2
            
            except:pass

            try:
                mobile1 = request.POST['mobile1']
                contact.mobile1  = mobile1
            except:pass

            try:
                mobile2 = request.POST['mobile2']
                contact.mobile2 = mobile2
            except:pass

            try:
                mobile3 = request.POST['mobile3']
                contact.mobile3 = mobile3
            except:pass

            try:
                website1 = request.POST['website1']
                contact.website1 = website1
            except:pass

            try:
                website2 = request.POST['website2']
                contact.website2 = website2
            except:pass
            
            try:
                website3 = request.POST['website3']
                contact.website3 = website3
            except:pass

            contact.save()
            messages.success(request,"Contact Page Updated")
        
        else:
            pass
        return redirect('contact_us_page')
    else:
        return redirect('admin-login')




@login_required
def add_blog(request):
    if request.user.is_staff:
        if request.method == "POST":
            heading = request.POST['heading']
            image = request.FILES['image']
            description = request.POST['description']

            blog = Blog(heading = heading,image = image,description = description)
            blog.save()
            blog_detail = Blog_Detail(sel_blog = blog)
            blog_detail.save()
            messages.success(request,'Blog Addedd Successfully')
        else:
            pass
        return render(request,'adminapp/add_blog.html')
    else:
        return redirect('admin-login')



@login_required
def blog_list(request):
    if request.user.is_staff:
        blog = Blog.objects.all()
        context = {
            'blog' : blog
        }
        return render(request,'adminapp/blog_list.html',context)
    else:
        return redirect('admin-login')


@login_required
def view_blog(request,myid):
    if request.user.is_staff:
        blog = Blog.objects.get(id = myid)
        context = {
            'blog' : blog
        }
        return render(request,'adminapp/add_blog.html',context)
    else:
        return redirect('admin-login')



@login_required
def update_blog_detail(request,myid):
    if request.user.is_staff:
        blog = Blog.objects.get(id = myid)
        blog_detail = Blog_Detail.objects.get(sel_blog = blog)
        if request.method == "POST":
            blog.heading = request.POST['heading']
            try:
                blog.image = request.FILES['image']
            except:pass

            blog.description = request.POST['description']
            
            try:
                blog_detail.video = request.FILES['video']
            except:pass

            try:
                blog_detail.doc_file = request.FILES['doc_file']
            except:pass

            blog_detail.write_blog = request.POST['write_blog']

            blog.save()
            blog_detail.save()
            messages.success(request,"Blog detail Updated Successfully")

        else:
            pass
        return redirect('blog_list')
    else:
        return redirect('admin-login')




@login_required
def delete_blog(request,myid):
    if request.user.is_staff:
        blog = Blog.objects.get(id = myid)
        blog.delete()
        messages.success(request,"Blog Deleted successfully")
        return redirect('blog_list')
    else:
        return redirect('admin-login')



@login_required
def project_enquiry_list(request):
    if request.user.is_staff:
        project_enq = Project_Enquiry.objects.all()
        context = {
            'enq' : project_enq
        }
        return render(request,'adminapp/project_enquiry_list.html',context)
    else:
        return redirect('admin-login')


@login_required
def add_seo_script(request):
    if request.user.is_staff:
        return render(request,'adminapp/add_seo_script.html')
    else:
        return redirect('admin-login')



@login_required
def keyward_list(request):
    if request.user.is_staff:
        key = Keywards.objects.all().last()
        context = {
            'key' : key
        }
        if request.method == "POST":
            keyward = request.POST['keyward']
            key.keyward = keyward
            key.save()
            messages.success(request,"Keywards Updated SUccessfully")
        else:
            pass

        return render(request,'adminapp/keyward_list.html',context)
    else:
        return redirect('admin-login')






@login_required
def about_us_page(request):
    if request.user.is_staff:
        if request.method == "POST":
            heading = request.POST['heading']
            description = request.POST['description']
            logo = request.FILES['logo']
            ab = About_Us_Items(heading = heading,description=description,logo = logo)
            ab.save()
            messages.success(request,"About Us Item Addedd Successfully")
        else:
            pass
        return render(request,'adminapp/about_us_page.html')
    else:
        return redirect('admin-login')







@login_required
def about_us_page_list(request):
    if request.user.is_staff:
        about_us_list = About_Us_Items.objects.all()
        context = {
            'about_us_list' :about_us_list
        }
        return render(request,'adminapp/about_us_page_list.html',context)
    else:
        return redirect('admin-login')





@login_required
def view_about_us(request,myid):
    if request.user.is_staff:
        about = About_Us_Items.objects.get(id = myid)
        context = {
            'about' : about
        }
        return render(request,'adminapp/about_us_page.html',context)
    else:
        return redirect('admin-login')


@login_required
def update_about_us_page(request,myid):
    if request.user.is_staff:
        about = About_Us_Items.objects.get(id= myid)
        if request.method == "POST":
            about.heading = request.POST['heading']
            about.description = request.POST['description']
            try:
                about.logo = request.FILES['logo']
            except:
                pass
            about.save()
            messages.success(request,"About Us item Updated SUccessfully")
        else:
            pass
        return redirect('about_us_page_list')
    else:
        return redirect('admin-login')


@login_required
def delete_about_item(request,myid):
    if request.user.is_staff:
        ab = About_Us_Items.objects.get(id = myid)
        ab.delete()
        messages.success(request,"about us Item Deleted Successfully")  
        return redirect('about_us_page_list')
    else:
        return redirect('admin-login')


@login_required
def user_enquiry_list(request):
    if request.user.is_staff:
        enq = Student_Enquiry.objects.all()[::-1]
        context = {
            'enq' : enq
        }
        return render(request,'adminapp/user_enquiry_list.html',context)
    else:
        return redirect('admin-login')






@login_required
def sold_project_list(request):
    if request.user.is_staff:
        sold_pro = Purchased_Project.objects.all()[::-1]
        context = {
            'sold_pro' : sold_pro
        }
        return render(request,'adminapp/sold_project_list.html',context)
    else:
        return redirect('admin-login')






























