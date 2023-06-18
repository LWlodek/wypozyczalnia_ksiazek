from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages
from .models import Book
from .forms import BookForm, BorrowForm


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
    borrowed_books = Book.objects.filter(user=request.user, availability=False)
    return render(request, 'base/profile.html', {'user_profile': user_profile, 'books': borrowed_books})


@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured')
    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    all_books = Book.objects.all()
    return render(request, 'base/home.html', {'books': all_books})


@login_required
def borrow(request):
    available_books = Book.objects.filter(availability=True)
    choices = [(book.id, f'{book.id} - {book.title} - {book.author}') for book in available_books]
    form = BorrowForm(initial={'book_ids': choices})

    if request.method == 'POST':
        form = BorrowForm(request.POST)
        form.fields['book_ids'].choices = choices  # Aktualizacja dostępnych wyborów w formularzu
        if form.is_valid():
            book_ids = form.cleaned_data['book_ids']
            # Zmiana statusu dostępności książek na False
            Book.objects.filter(id__in=book_ids).update(availability=False)
            # Przypisanie wypożyczonych książek do użytkownika
            user = request.user
            for book_id in book_ids:
                book = Book.objects.get(id=book_id)
                book.user = user
                book.save()
            return redirect('profile')

    return render(request, 'base/borrow.html', {'books': available_books, 'form': form})


@user_passes_test(lambda u: u.is_superuser)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book-list')  # Przekierowanie po dodaniu książki
    else:
        form = BookForm()
    return render(request, 'base/add_book.html', {'form': form})


@login_required
def return_book(request):
    context = {}
    return render(request, 'base/return_book.html', context)


def book_list(request):
    all_books = Book.objects.all()
    return render(request, 'base/book_list.html', {'books': all_books})



