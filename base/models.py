from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    borrowed_books = models.ManyToManyField(Book, through='BorrowedBook')
    # Dodać pozostałe pola profilu użytkownika, np. dane kontaktowe, rezerwacje

    def __str__(self):
        return self.user.username


class BorrowedBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.book.title}"