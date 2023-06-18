from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'availability')
    list_editable = ('availability',)
    list_display_links = ('title', 'author')
    list_filter = ('availability',)  # filtr do panelu bocznego dla pola availability
    search_fields = ('title', 'author')  # pole wyszukiwania dla tytułu i autora

