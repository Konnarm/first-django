from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^books/$', views.BookIndexView.as_view(), name='books_index'),
    url(r'^writer/(?P<pk>[0-9]+)/$', views.WriterDetailView.as_view(), name='writer_detail'),
    url(r'^writer/add/$', views.WriterCreate.as_view(), name='writer-add'),
    url(r'^writer/update/(?P<pk>[0-9]+)/$', views.WriterUpdate.as_view(), name='writer-update'),
    url(r'^writer/(?P<pk>[0-9]+)/delete/$', views.WriterDelete.as_view(), name='writer-delete'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^book/add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'^book/update/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book-update'),
    url(r'^book/(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
]