from django.shortcuts import render, get_object_or_404

from .models import Book


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
