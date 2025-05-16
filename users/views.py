from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser  # ✅ Use your custom user model
from django.contrib.auth.decorators import login_required

# LOGIN
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home/dashboard
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'users/login.html')

# SIGNUP
def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'users/signup.html')

# LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')

# HOME (Dashboard)
@login_required(login_url='login')
def home(request):
    return render(request, 'users/home.html')
