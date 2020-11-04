from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,label="Password")

class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,label="Password")