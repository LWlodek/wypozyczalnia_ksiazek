from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

books = [
    {'id': 1, 'name': 'Pan tadeusz'},
    {'id': 2, 'name': 'Pani tadeusz'},
    {'id': 3, 'name': 'Panowie tadeusz'},
]

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    context = {'books': books}
    return render(request, 'base/home.html', context)

def rent(request):
    return render(request,'base/rent.html')

