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
    path('blog/create/', views.create_blog, name="create_blog"),
    path('<int:blog_id>/blog/delete/', views.delete_blog, name="delete_blog"),
    path('<int:blog_id>/blog/edit_page/', views.edit_blog_page, name="edit_blog_page"),
    path('<int:blog_id>/blog/edit/', views.edit_blog, name="edit_blog"),
    path('<int:blog_id>/blog/comment/', views.comment, name="comment"),
    path('<int:blog_id>/blog/comments/', views.comments_page, name="comments_page")
     
]