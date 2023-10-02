from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "title", "slug", "status", "description"]
    prepopulated_fields = {"slug":  ("author", "title")}
