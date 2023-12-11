from django.shortcuts import render,redirect
from courseapp .models import *
from .models import *
# Create your views here.


def Practice_problems(request,myid):
    try:
        sub = Subject.objects.get(id = myid)
        # chapter = Chapter.objects.filter(sel_subject = sub)
        program_list = Practice_program.objects.filter(sel_subject = sub)

        context = {
            'sub':sub,
            'program_list': program_list
        }
        return render(request,'practiceapp/practice_problem.html',context)

    except:
        return redirect('error_page')





def Practice_list(request):
    try:
        subject = Subject.objects.all()
        context = {
            'subject' : subject
        }
        return render(request,'practiceapp/practice_list.html',context)
    except:
        return redirect('error_page')




def Program_data(request,subid,myid):
    try:
        sub = Subject.objects.get(id = subid)
        
        program_list = Practice_program.objects.filter(sel_subject = sub)
        program_data = Practice_program.objects.get(id = myid)
        context = {
            'sub':sub,
            'program_list' : program_list,
            'program_data' : program_data
        }
        return render(request,'practiceapp/practice_problem.html',context)  
    except:
        return redirect('error_page')