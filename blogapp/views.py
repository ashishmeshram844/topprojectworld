from django.shortcuts import render
from .models import *
# Create your views here.
from django.core.paginator import Paginator





def Blogs(request):
    blogg = Blog.objects.all()

  
    paginator = Paginator(blogg, 5)
    page_number = request.GET.get('page')
    blog = paginator.get_page(page_number)
    context = {
        'blog' : blog
    }
    return render(request,'blogapp/blogs.html',context)





def Blogs_detail(request,myid):
    blog = Blog.objects.get(id = myid)
    blog_detail = Blog_Detail.objects.get(sel_blog = blog)
    context = {
        'blog_detail' : blog_detail
    }
    return render(request,'blogapp/blogs_detail.html',context)