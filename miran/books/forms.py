from django import forms
from .models import Book


class BookSearchForm(forms.Form):
    search = forms.CharField(max_length=100,
                             required=False)


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'description', 'year')
