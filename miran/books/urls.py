from django.urls import path

from . import views

app_name = 'books'


urlpatterns = [
    path("list/", views.list_books, name="list_books"),
    path("detail/<slug:slug>/", views.detail, name="detail"),
    path('reg_book/', views.reg_book, name='reg_book'),
    path('return_book/', views.return_book, name='return_book'),
]
