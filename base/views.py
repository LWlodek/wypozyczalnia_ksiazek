from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages
from .models import Book, UserProfile
from .forms import BookForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

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

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


@login_required
def profile(request):
    user_profile = request.user.username
    # context = {}
    return render(request, 'base/profile.html', {'user_profile': user_profile})


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # Tworzenie profilu użytkownika
            # UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured')
    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    # context = {'books': books}
    available_books = Book.objects.filter(availability=True)
    return render(request, 'base/home.html', {'books': available_books})


def rent(request):
    return render(request, 'base/rent.html')


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book-list')  # Przekierowanie po dodaniu książki
    else:
        form = BookForm()
    return render(request, 'base/add_book.html', {'form': form})


def return_book(request):
    return render(request, 'base/return_book.html')


def book_list(request):
    available_books = Book.objects.filter(availability=True)
    return render(request, 'base/book_list.html', {'books': available_books})



