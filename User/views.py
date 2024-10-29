from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import SignupForm
from django.urls import reverse

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'User/login.html', {'form' : form})

def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'User/signup.html', {'form' : form})

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return redirect(reverse('login'))

    return render(request, 'User/profile.html', {'username': username})