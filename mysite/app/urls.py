from django.urls import path, re_path
from app import views
from django.conf.urls import url

from django.contrib.auth import views as auth_views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name=''), name='logout'),

    path('loan_app_success.html', views.loan_app_success, name='loan_app_success'),
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),
]
