"""TopicsManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from Topics import views
from Topics.forms import LoginForm, EmailValidationOnForgotPassword

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'Topics/login.html', 'authentication_form': LoginForm,
                                        'redirect_authenticated_user': True},
        name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^add_topic/$', views.add_topic, name='add_topic'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

    url(r'^account/password_reset/$', auth_views.password_reset,
        {'template_name': 'Topics/password_reset/password_reset_form.html',
         'post_reset_redirect': 'password_reset_done',
         'password_reset_form': EmailValidationOnForgotPassword}, name='password_reset'),
    url(r'^account/password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'Topics/password_reset/password_reset_done.html'}, name='password_reset_done'),
    url(r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'Topics/password_reset/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^account/reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'Topics/password_reset/password_reset_complete.html'}, name='password_reset_complete'),

]