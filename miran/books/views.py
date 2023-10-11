from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from users.models import User


def list_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request=request,
                  template_name="books/list_books.html",
                  context=context)


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        "book": book
    }
    return render(request=request,
                  template_name="books/detail_book.html",
                  context=context)


def reg_book(request):
    if request.method == 'POST':
        slug = request.POST.get("slug", None)
        print(request.user.username)
        user = get_object_or_404(User, username=request.user.username)
        book = Book.objects.get(slug=slug)
        book.status = Book.Status.CLOSE
        book.save()
        context = {"user": user,
                   "book": book}
    else:
        context = {"user": '',
                   "book": ''}
    return render(request=request,
                  template_name="books/reg_book.html",
                  context=context)
