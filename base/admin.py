from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'availability', 'user')
    list_editable = ('availability',)
    list_display_links = ('title', 'author')
    list_filter = ('availability', 'user')
    search_fields = ('title', 'author', 'user__username')

    def borrowed_by(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return "N/A"



