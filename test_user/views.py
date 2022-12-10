from django.shortcuts import render,redirect
from user_account.forms import *
from user_account import models
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegisterForm


from django.contrib.auth.forms import PasswordChangeForm


def index(request):
    users = models.User.objects.all()
    return render(request,'index.html',{'users':users})

def create_user(request):
    form = forms.UserCreationForm()
    if request.method=='POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid :
            form.save()
        return redirect('index')
    else :
         form = forms.UserCreationForm()
    return render(request, 'create_user.html', {'form':form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
    

def register_user(request):
    
    if request.method=='POST':
        form = RegisterForm(request.POST)
        # pass1= request.POST['repassword']
        # pass2= request.POST['password']
        
        if form.is_valid :
            data = request.POST
            if data['password'] == data['repassword'] :
                user = User.objects.create_superuser(email=data['email'],
                                                     phone=data['phone'],
                                                     username=data['username'],
                                                     password=data['password'])
                
                return redirect('index')
            else:
                print("dont match")
            
    else :
        
        form = RegisterForm()
         
    return render(request, 'register.html', {'form':form})
        
