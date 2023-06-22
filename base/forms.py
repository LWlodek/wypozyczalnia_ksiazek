from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'availability', ]


class BorrowForm(forms.Form):
    book_ids = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)