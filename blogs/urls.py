from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog_page, name="blog_page"),
    path('signup_form/', views.signup_form, name="signup_form"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('login_form/', views.login_form, name="login_form"),
    path('user_login/', views.user_login, name="user_login"),
    path ('user_logout/', views.logout, name="user_logout"),
    path('blog/create/', views.create_blog, name="create_blog")
     
]