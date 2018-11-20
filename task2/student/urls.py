from django.conf.urls import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.student_index, name='student_index'),
    path('registration/', views.registration, name='registration'),
    # url(r'^login/$', auth_views.login, {'template_name': 'student/login.html'}, name='login'),

    path('login/',auth_views.LoginView.as_view(template_name=''),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name=''),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name=''),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name=''),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name=''),name='password_reset_done'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name=''),name='password_reset_complete'),
    path('signup/', views.signup, name='signup'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('fees/', views.fees, name='fees'),
    path('calculate_fees', views.calculate_fees, name='calculate_fees'),
    path('final_amount', views.final_amount, name='final_amount'),
    path('add_fees', views.add_fees, name='add_fees'),
    path('render_pdf_view', views.render_pdf_view, name='render_pdf_view'),


    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

    # path('logout/',auth_views.LogoutView.as_view(template_name='student/logout.html'),name='login'),
