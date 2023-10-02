from django.urls import path

from . import views

app_name = 'books'


urlpatterns = [
    path("list/", views.list_books, name="list_books"),
    path("detail/<slug:slug>/", views.detail, name="detail"),
]