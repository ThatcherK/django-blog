from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request,'blogs/home.html',{'username': username})

def blog_page(request):
    return render(request, 'blogs/create_blog.html', context=None)

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
    return render(request,'blogs/home.html',context=None)