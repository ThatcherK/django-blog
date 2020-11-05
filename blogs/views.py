from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, LoginForm, BlogForm, EditBlogForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Blog

def index(request):
    username = None
    blog_list = None
    if request.user:
        username = request.user.username
        blog_list = Blog.objects.all()
    return render(request,'blogs/home.html',{'username': username, 'blog_list':blog_list})

def blog_page(request):
    form =BlogForm()
    return render(request, 'blogs/create_blog.html', {"form": form})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                title = form.cleaned_data.get('title')
                body = form.cleaned_data.get('body')
                picture = form.cleaned_data.get('picture')
                if picture is not None:
                    blog = Blog(title=title, body=body, picture=picture, user=request.user)
                    blog.save()
                else:
                    blog = Blog(title=title, body=body, user=request.user)
                    blog.save() 
                return redirect(reverse('index'))
            else:
                return HttpResponse('Please log in')
        else:
            form = BlogForm()

def delete_blog(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if blog is not None:
        blog.delete()
        return redirect(reverse('index'))

def edit_blog_page(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    
    if blog is not None:
        intial_data = {
            'title': blog.title,
            'body':blog.body,
            'picture': blog.picture
        }
        form = EditBlogForm(initial=intial_data)
        return render(request,'blogs/edit_blog.html',{'form': form, "blog": blog})

def edit_blog(request, blog_id):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                title = form.cleaned_data.get('title')
                body = form.cleaned_data.get('body')
                picture = form.cleaned_data.get('picture')
                
                blog = Blog.objects.get(pk=blog_id)
                if blog is not None:
                    blog.title = title
                    blog.body = body
                    blog.picture = picture
                    blog.save()
                return redirect(reverse('index'))
            else:
                return HttpResponse('Please log in')
        else:
            form = BlogForm()
def signup_form(request):
    form = SignupForm()
    return render(request, 'blogs/signup.html', context={'form': form})
  
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            try:
                user_check = User.objects.get(username=username)
                return HttpResponse("User already exists")
            except User.DoesNotExist:

                user = User.objects.create_user(username=username, password=password)
                user.save()
                print(user)
                return redirect(reverse('index'))

def login_form(request):
    form = LoginForm()
    return render(request, 'blogs/login.html', context={'form': form})

def user_login(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse('Invalid log in')

def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

