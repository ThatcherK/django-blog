from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,label="Password")

class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,label="Password")

class BlogForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField(required=False)

class EditBlogForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField(required=False)

class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=100)