from django.db import models
from django.core.urlresolvers import reverse

class Writer(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    writer_photo = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('books:writer_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + " - " + self.nationality

class Book(models.Model):
    book_title = models.CharField(max_length=40)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    book_cover = models.CharField(max_length=300)
    genre = models.CharField(max_length=20)
    series = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.book_title