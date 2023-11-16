from datetime import timedelta
import time
from pathlib import Path

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.conf import settings

from .models import Book, History
from .forms import BookSearchForm, AddBookForm, EditBookForm
from users.models import User


def list_books(request):
    if request.method == "POST":
        form = BookSearchForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            title = form.cleaned_data.get('title')
            status = form.cleaned_data.get('status')
            reader = form.cleaned_data.get('reader')
            books = Book.objects.filter(
                Q(author__icontains=author) | Q(title__icontains=title)
            )
            context = {
                "books": books,
                "form": BookSearchForm(data=request.POST),
            }
        return render(request=request,
                      template_name="books/list_books.html",
                      context=context)

    context = {
        "books": Book.objects.all(),
        "form": BookSearchForm(),
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

    if request.user.is_staff:
        return render(request=request,
                      template_name="books/detail_book_staff.html",
                      context=context)

    return render(request=request,
                  template_name="books/detail_book.html",
                  context=context)


def get_book(request):
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


def add_book(request):
    if request.method == "POST":
        form = AddBookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get("author", '')
            title = form.cleaned_data.get("title", '')
            description = form.cleaned_data.get("description", '')
            year = form.cleaned_data.get("year", 0)
            Book.objects.create(author=author,
                                title=title,
                                description=description,
                                year=year)
            return redirect(to=reverse("books:list_books"))

    else:
        form = AddBookForm()
    context = {
        "form": form,
    }
    return render(request=request,
                  template_name='books/add_book.html',
                  context=context)


def edit_book(request, slug):
    book = Book.objects.get(slug=slug)

    if request.method == "POST":
        form = EditBookForm(data=request.POST)
        if form.is_valid():
            book.author = form.cleaned_data.get("author")
            book.title = form.cleaned_data.get("title")
            book.year = form.cleaned_data.get("year")
            book.description = form.cleaned_data.get("description")
            book.save()
            return redirect(to="books:list_books")

    form = EditBookForm(instance=book)
    context = {
        "form": form,
    }
    return render(request=request,
                  template_name="books/edit_book.html",
                  context=context)


def delete_book(request, slug):
    try:
        book = Book.objects.get(slug=slug)
        # file = Path(f"{str(settings.MEDIA_ROOT)}\\books\\{str(book.qr_code)[6:]}")
        # file.unlink()
        book.delete()
        return redirect(to="books:list_books")
    except Exception:
        return HttpResponseNotFound("<h2>Невозможно удалить</h2>")
