from django.urls import path

from . import views

app_name = 'books'


urlpatterns = [
    path("list/", views.list_books, name="list_books"),
    path("detail/<slug:slug>/", views.detail, name="detail"),
    path('reg_book/', views.reg_book, name='reg_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('list_qr/', views.list_qr, name='list_qr'),
    # path('edit/<slug:slug>/', views.EditBook.as_view(), name='edit'),
    path('edit/<slug:slug>/', views.edit_book, name='edit'),
    path('delete/<slug:slug>/', views.delete_book, name='delete'),
]
