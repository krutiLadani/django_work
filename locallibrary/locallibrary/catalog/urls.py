from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^books/$', views.BookListView.as_view(), name='books'),
url(r'^(?P<pk>\d+)/book/$', views.book_detail_view, name='book-detail'),
]
