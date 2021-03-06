from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.details, name='detail'),
    # url(r'^(?P<pk>[0-9]+)/$', views.detail, name='details'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='result'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
