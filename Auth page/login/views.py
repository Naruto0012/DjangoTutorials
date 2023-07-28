from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login, authenticate,logout  # add to imports

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login') # Replace 'login' with the URL name of your login view
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')