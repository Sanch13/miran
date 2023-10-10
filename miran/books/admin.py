from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "title", "status", "description"]
    exclude = ["slug", "qr_code"]
    list_display_links = ["author", "title"]
