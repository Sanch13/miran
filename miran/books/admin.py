from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "year", "description"]
    exclude = ["slug", "status", "reader", ]
    list_display_links = ["author", "title", "year"]
