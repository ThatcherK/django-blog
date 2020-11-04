from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User

def index(request):
    return render(request,'blogs/base.html',context=None)

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
            user_check = get_object_or_404(User, username=username)
            if user_check is not None:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return HttpResponse("Signup successful")
            else:
                return HttpResponse("Username already exists")