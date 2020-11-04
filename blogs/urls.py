from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog_page, name="blog_page"),
    path('signup_form/', views.signup_form, name="signup_form"),
    path('user_signup/', views.user_signup, name="user_signup")
     
]