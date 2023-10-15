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
        "books": books
    }
    return render(request=request,
                  template_name="books/list_books.html",
                  context=context)


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if book.status == "CLOSE":
        book_user = History.objects.filter(book=book).order_by("date_start").last()
        # book_user = History.objects.filter(book=book).order_by("-date_start").first()
        # book_user = History.objects.filter(book=book).annotate(last_book=Max("date_start")).last()
        print(request.user.id)
        print(book_user.user_id)
        print(book_user.date_start)
        context = {
            "book": book,
            "book_user": book_user,
        }
    else:
        context = {
            "book": book,
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
        book.save()
        History.objects.create(user=user,
                               book=book,
                               date_start=timezone.now() + timedelta(hours=3))
        context = {"user": user,
                   "book": book}
    return render(request=request,
                  template_name="books/reg_book.html",
                  context={})


def return_book(request):
    if request.method == 'POST':
        slug = request.POST.get("slug", None)
        book = get_object_or_404(Book, slug=slug)
        print(type(book), book.pk, book.id)
        book.status = Book.Status.OPEN
        book.save()

        user = get_object_or_404(User, username=request.user.username)
        print(type(user), user.pk, user.id)

        user_history = History.objects.filter(user=user, book=book).order_by("date_start").last()
        user_history.date_end = timezone.now() + timedelta(hours=3)
        user_history.save()

        messages.success(request=request, message="Вы успешно вернули книгу в библиотеку")
        return redirect(reverse(viewname="books:detail", args=[slug], ))
        # return render(request=request,
        #               template_name="books/return_book.html")
