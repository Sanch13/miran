from django.urls import path

from .views import *

app_name = 'books'


urlpatterns = [
    path("list_books/", list_books, name="list_books"),
    path("list_books/", list_books, name="list_books"),
]