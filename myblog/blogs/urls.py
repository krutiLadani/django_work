from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^post/(?P<post_id>\d+)$',views.postdetail,),
url(r'^post/$', views.post_upload, name='post_upload'),
url(r'^post/$',views.post_form_upload, name='post_form_upload'),
url(r'^post/new/$', views.post_new, name='post_new'),
]
