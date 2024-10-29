from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import SignupForm, LoginForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "User/login.html", {"form": form})


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "User/signup.html", {"form": form})


def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return redirect("login")

    return render(request, "User/profile.html", {"username": username})
