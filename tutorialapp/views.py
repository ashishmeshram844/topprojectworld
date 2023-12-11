from django.shortcuts import render,redirect,HttpResponse
from courseapp .models import *
from .models import *
from practiceapp .models import *
# Create your views here.


def Tutorial_languages(request):
    try:
        subject = Subject.objects.all()
        context = {
            'subject':subject
        }
        return render(request,'tutorialapp/tutorial_languages.html',context)

    except:
        return redirect('error_page')



def Tutorial_select_language(request,myid):
    try:
        sub = Subject.objects.get(id = myid)
        chapter = Chapter.objects.filter(sel_subject = sub)
        topic = Topic.objects.filter(sel_subject = sub)


        context={
            'sub':sub,
            'topic':topic

        }
        return render(request,'tutorialapp/tutorial_select_language.html',context)
    except:
        return redirect('error_page')





def Explore_topic(request,subid,myid):
    try:
        sub = Subject.objects.get(id = subid)
        chapter = Chapter.objects.filter(sel_subject = sub)
        topic = Topic.objects.filter(sel_subject = sub)
        topic_data = Topic.objects.get(id = myid)
        topic_tutorial = Tutorial_Detail.objects.filter(sel_topic = topic_data)


        last_topic_id = Topic.objects.filter(sel_subject = sub).last()
        next_topic_id = myid+1
        previous_topic_id = myid -1
        if next_topic_id > last_topic_id.id:
            next_topic_id = 0

        context={
            'sub':sub,
            'topic':topic,
            'topic_data' : topic_data,
            'topic_tutorial' : topic_tutorial,
            'next_topic_id' : next_topic_id,
            'previous_topic_id' : previous_topic_id

        }


        return render(request,'tutorialapp/tutorial_select_language.html',context)
    except:
        return HttpResponse('<script>alert("Topic Not Found Please Use sidebar to jump on next topica");window.history.back();</script>')