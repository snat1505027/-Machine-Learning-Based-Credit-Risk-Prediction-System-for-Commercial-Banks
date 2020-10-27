from django.urls import path, re_path
from employee import views


from django.urls import include


from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    #path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generatePrediction/<int:loan_id>/', views.generatePrediction, name='generatePrediction'),
    path('FRList/', views.FRList, name='FRList'),
    path('', auth_views.LoginView.as_view(template_name='employee/login.html'), name='login'),
    path('getCSV/<int:loan_id>/', views.getCSV, name='getCSV'),
    path('logout_emp/', auth_views.LogoutView.as_view(template_name='employee/login.html'), name='logout_emp'),
    path('form_reviewer_reject/<int:CarLoanApplication_pk>/', views.form_reviewer_reject, name='form_reviewer_reject'),
    path('NList/', views.NList, name='NList'),
    path('profile/', views.profile, name='profile'),
    path('tempChart/', views.tempChart, name='tempChart'),
    path('defaulter/', views.defaulter, name='defaulter'),
    path('interestRate/', views.interestRate, name='interestRate'),
    path('CRMList/', views.CRMList, name='CRMList'),
    path('ATables/', views.ATables, name='ATables'),
    path('LHistory/', views.LHistory, name='LHistory'),
    path('update_amount/<int:CarLoanApplication_pk>/', views.update_amount, name='update_amount'),
    path('crm_accept/<int:loan_account_id_pk>/',views.crm_accept, name='crm_accept'),
    path('crm_reject/<int:loan_account_id_pk>/', views.crm_reject,name='crm_reject'),
    path('nego_reject/<int:CarLoanApplication_pk>/',views.nego_reject,name='nego_reject'),
]
