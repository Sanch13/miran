from datetime import timedelta
from pathlib import Path

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

from .models import Book, History
from .forms import BookSearchForm, AddBookForm, EditBookForm
from users.models import User


def list_books(request):
    books = Book.objects.all()

    if request.GET:
        if 'clear_filter' in request.GET:
            return redirect('books:book_list_card')

        form = BookSearchForm(data=request.GET)
        if form.is_valid():
            author = form.cleaned_data.get('author', '')
            title = form.cleaned_data.get('title', '')
            status = form.cleaned_data.get('status', '')
            reader = form.cleaned_data.get('reader', '')
            books = form.filter_books(queryset=books)

            form = BookSearchForm(initial={
                "author": author,
                "title": title,
                "status": status,
                "reader": reader
            })
    else:
        form = BookSearchForm()
    context = {'books': books, 'form': form}
    return render(request=request,
                  template_name="books/book_list_card.html",
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
        form = AddBookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            author = form.cleaned_data.get("author", '')
            title = form.cleaned_data.get("title", '')
            description = form.cleaned_data.get("description", '')
            label = form.cleaned_data.get("label", '')
            year = form.cleaned_data.get("year", 0)
            try:
                book = Book.objects.create(author=author,
                                           title=title,
                                           description=description,
                                           label=label,
                                           year=year)
                return redirect(reverse(viewname="books:detail", args=[book.slug], ))
            except Exception:
                return 'Не удалось'

    else:
        form = AddBookForm()
    context = {
        "form": form,
    }
    return render(request=request,
                  template_name='books/add_book.html',
                  context=context)


def print_qr(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request=request,
                  template_name='books/print_qr.html',
                  context=context)


def print_selected_qr(request):
    if request.method == 'GET':
        selected_books = request.GET.getlist('selectedBooks[]')
        context = {
            "books": Book.objects.filter(id__in=selected_books)
        }
        return render(request=request,
                      template_name='books/print_selected_qr.html',
                      context=context)


def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if request.method == "POST":
        form = EditBookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            book.author = form.cleaned_data.get("author")
            book.title = form.cleaned_data.get("title")
            book.year = form.cleaned_data.get("year")
            book.description = form.cleaned_data.get("description")
            book.label = form.cleaned_data.get("label") or book.label
            book.save()
            return redirect(reverse(viewname="books:detail", args=[book.slug], ))

    form = EditBookForm(instance=book)
    context = {
        "form": form,
    }
    return render(request=request,
                  template_name="books/edit_book.html",
                  context=context)


def delete_book(request, slug):
    try:
        book = get_object_or_404(Book, slug=slug)
        file = Path(f"{str(settings.MEDIA_ROOT)}/{str(book.qr_code)}")
        file.unlink(missing_ok=True)
        label = Path(f"{str(settings.MEDIA_ROOT)}/{str(book.label)}")
        label.unlink(missing_ok=True)
        book.delete()
        return redirect(to="books:book_list_card")
    except Exception:
        return HttpResponseNotFound("<h2>Невозможно удалить книгу</h2>")
