from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('todo_list')  # Replace with your homepage route
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'base/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('user_login')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('user_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('user_register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Account created successfully. Please login.")
        return redirect('user_login')

    return render(request, 'base/register.html')
