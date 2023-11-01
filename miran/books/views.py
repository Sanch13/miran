from datetime import timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse

from .models import Book, History
from users.models import User


def list_books(request):
    books = Book.objects.all()

    context = {
        "books": books,
    }
    return render(request=request,
                  template_name="books/list_books.html",
                  context=context)


def detail(request, slug):
    # Если user не авторизован запоминаем url
    if not request.user.is_authenticated:
        request.session['next_url'] = request.get_full_path()

    book = get_object_or_404(Book, slug=slug)
    book_history = History.objects.filter(book=book)

    context = {
        "book": book,
        "book_history": book_history,
        "reader": History.objects.filter(book=book).order_by("date_start").last() if
        book.status == "CLOSE" else ''
    }

    return render(request=request,
                  template_name="books/detail_book.html",
                  context=context)


def reg_book(request):
    if request.method == 'POST':
        slug = request.POST.get("slug", None)
        user = get_object_or_404(User, username=request.user.username)
        book = Book.objects.get(slug=slug)
        book.status = Book.Status.CLOSE
        book.reader = str(user)
        book.save()

        History.objects.create(user=user,
                               book=book,
                               date_start=timezone.now() + timedelta(hours=3))
        messages.success(request=request,
                         message="Вы успешно взяли книгу из библиотеки")
        return redirect(reverse(viewname="books:detail", args=[slug], ))


def return_book(request):
    if request.method == 'POST':
        slug = request.POST.get("slug", None)
        book = get_object_or_404(Book, slug=slug)
        book.status = Book.Status.OPEN
        book.reader = ''
        book.save()

        user = get_object_or_404(User, username=request.user.username)

        user_history = History.objects.filter(user=user, book=book).order_by("date_start").last()
        user_history.date_end = timezone.now() + timedelta(hours=3)
        user_history.save()

        messages.success(request=request,
                         message="Вы успешно вернули книгу в библиотеку")
        return redirect(reverse(viewname="books:detail", args=[slug], ))
