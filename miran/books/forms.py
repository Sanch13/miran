from django import forms

from .models import Book


class BookSearchForm(forms.ModelForm):
    author = forms.CharField(required=False)
    title = forms.CharField(required=False)
    STATUS_CHOICES = [('', '------------------'), ('OPEN', 'Свободна'), ('CLOSE', 'В пользовании')]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус книги")

    def filter_books(self, queryset):
        author = self.cleaned_data.get('author')
        title = self.cleaned_data.get('title')
        status = self.cleaned_data.get('status')
        reader = self.cleaned_data.get('reader')

        if author:
            queryset = queryset.filter(author__icontains=author)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if status:
            queryset = queryset.filter(status=status)
        if reader:
            queryset = queryset.filter(reader__icontains=reader)

        return queryset

    class Meta:
        model = Book
        fields = ('author', 'title', 'status', 'reader')

    def __init__(self, *args, **kwargs):
        super(BookSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'description', 'year', 'label')

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'year', 'description')

    def __init__(self, *args, **kwargs):
        super(EditBookForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
