from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth import login, authenticate,logout



def Login(request):
    
    if request.method == 'POST':
        # Create an instance of AuthenticationForm with the submitted data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authentication successful, login the user
            user = form.get_user()
            login(request, user)
            return redirect('/project/all')  # Replace 'dashboard' with the URL name of your desired page after login
        else:
            # Handle invalid login attempt
            context = {
                'form': form,
                'error_message': 'Invalid username or password. Please try again.',
            }
            return render(request, 'login.html', context)
    else:
        # Render the login page template for GET requests
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

  #method2
  def Login(request):
    if request.method == 'POST':
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=form.cleaned_data[username], password=form.cleaned_data[password])
            if user is not None:
                auth.login(request, user)
                return redirect('project') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#method3
def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/project/all') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form}) """
