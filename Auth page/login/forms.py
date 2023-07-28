from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)
	help_text=''
	

class LoginForm(AuthenticationForm):
    pass