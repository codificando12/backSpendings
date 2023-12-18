from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        try:
          validate_email(email)
        except ValidationError:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Please enter a valid email'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Email already taken. Please choose a new email'})
        
        if len(password1) < 8:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Password too short. Password must be at least 8 characters'})

        if password1 == password2:
            try:
                user = User.objects.create_user(username, password1, email)
                user.save()
                login(request, user)
                return redirect('groups')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Username already taken. Please choose a new username'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Passwords did not match'})
        
def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm, 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')	