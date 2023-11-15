from django import forms
from .models import Book


class BookSearchForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'status', 'reader')
    # search = forms.CharField(max_length=100,
    #                          required=False)


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title', 'description', 'year')

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

