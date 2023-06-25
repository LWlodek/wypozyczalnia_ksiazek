from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime
import pytz


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class BorrowedBook(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='books_borrowed')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='borrowed_books')
    borrowed_date = models.DateTimeField(default=datetime.now())
    return_to_date = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.book.title}"
