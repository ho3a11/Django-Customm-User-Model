from django import forms
from user_account.models import User
from django.core.exceptions import ValidationError



class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=50,label='UserName')
    phone = forms.IntegerField(label='Phone Number')
    is_active = forms.BooleanField(label='activate')
    is_admin = forms.BooleanField(label='Set Admin')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repassword = forms.CharField(label='RePassword', widget=forms.PasswordInput)
        
