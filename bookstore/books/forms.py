from django import forms

from .models import Writer, Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['book_title', 'writer', 'book_cover', 'genre', 'series']