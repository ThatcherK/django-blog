from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'blogs/base.html',context=None)

def blog_page(request):
    return render(request, 'blogs/create_blog.html', context=None)