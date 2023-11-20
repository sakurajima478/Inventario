from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

from .forms import UserRegisterForm, ContactForm

def home_view(request):
    return render(request, 'core/home.html')

def about_view(request):
    return render(request, 'core/about.html')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'core/register.html', {
            'form' : UserRegisterForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                messages.success(request, 'User Register Sucessfully')
                return redirect('home')
            except IntegrityError:
                messages.warning(request, 'User already exists')
                return render(request, 'core/register.html', {
                    'form' : UserRegisterForm,
                })
                
        messages.warning(request, 'Password do not match')
        return render(request, 'core/register.html', {
            'form' : UserRegisterForm,
        })

def login_view(request):
    if request.method == 'GET':
        return render(request, 'core/login.html', {
            'form' : AuthenticationForm,
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.warning(request, 'Username or Password is incorrect')
            return render(request, 'core/login.html', {
                'form' : AuthenticationForm,
            })
        else:
            login(request, user)
            return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')