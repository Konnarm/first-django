from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Writer, Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = "all_writers"

    def get_queryset(self):
        return Writer.objects.all()

class WriterDetailView(generic.DetailView):
    model = Writer
    template_name = 'books/writer_detail.html'

    def get_queryset(self):
        return Writer.objects.all()

class BookIndexView(generic.ListView):
    template_name = 'books/book_index.html'
    context_object_name = "all_books"

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_queryset(self):
        return Book.objects.all()

class WriterCreate(CreateView):
    model = Writer
    fields = ['name', 'genre', 'nationality', 'writer_photo']

class WriterUpdate(UpdateView):
    model = Writer
    fields = ['name', 'genre', 'nationality', 'writer_photo']

class WriterDelete(DeleteView):
    model = Writer
    success_url = reverse_lazy('books:index')

class BookCreate(CreateView):
    model = Book
    fields = ['book_title', 'writer', 'book_cover', 'genre', 'series']

class BookUpdate(UpdateView):
    model = Book
    fields = ['book_title', 'writer', 'book_cover', 'genre', 'series']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books_index')
