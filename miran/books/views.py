from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book


def list_books(request):
    books = Book.objects.all()
    return render(request=request)


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request=request,
                  template_name="",
                  context={"book": book})
