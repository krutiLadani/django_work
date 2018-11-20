from django.conf.urls import url, include
from shop import views
from django.contrib import admin
from shop.views import GeneratePDF
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart/$', views.add_cart, name='cart'),
    url(r'^checkout/$', views.order, name='order'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^(?P<pk>[0-9]+)/details/$', views.details, name='details'),
    url(r'^add_to_cart$', views.add_to_cart, name='add_to_cart'),
    url(r'^(?P<product_id>[0-9]+)/remove$', views.cart_remove, name='cart_remove'),
    url(r'^pdf/$', views.GeneratePDF.as_view(), name='pdf'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url('^accounts/', include('django.contrib.auth.urls', namespace="auth")),
]

