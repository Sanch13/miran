from django.urls import path

from . import views

app_name = 'books'


urlpatterns = [
    path("list/", views.list_books, name="book_list_card"),
    path("detail/<slug:slug>/", views.detail, name="detail"),
    path('get_book/', views.get_book, name='get_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('print_qr/', views.print_qr, name='print_qr'),
    path('print_selected_qr/', views.print_selected_qr, name='print_selected_qr'),
    path('edit/<slug:slug>/', views.edit_book, name='edit'),
    path('delete/<slug:slug>/', views.delete_book, name='delete'),
    path("taken_books/", views.show_taken_books, name="taken_books")
]
