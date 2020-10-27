from django.urls import path
from . import views
from django.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views



from django.contrib.auth.views import (
PasswordResetView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetCompleteView,
PasswordChangeView,
PasswordChangeDoneView,
)


urlpatterns = [
	path('', views.homepage, name='homepage'),
    path('', views.homepage, name='home'),
    path('verification/', views.verification, name='verification'),
    path('messages/', include('postman.urls')),
    url(r'^login_success/$', views.login_success, name='login_success'),
    path('app/',include('app.urls')),
    
    path('handleForm/', views.handleForm , name='handleForm'),
    
    path('history/', views.history, name='history'),


   path('loanApplicationForm/', views.loanApplicationForm, name='loanApplicationForm'),

   path('loanApplicationForm/lafp2/', views.lafp2, name='lafp2'),

   path('lafp3/', views.lafp3, name='lafp3'),

   path('showGraph/', views.showGraph, name='showGraph'),

   path('edit_profile/', views.edit_profile, name='edit_profile'),

   path('carloan4/', views.carloan4, name='carloan4'),

   path('carloan5/', views.carloan5, name='carloan5'),

    path('generatePrediction/<int:loan_id>/', views.generatePrediction, name='generatePrediction'),

    path('negotiate_client/', views.negotiate_client, name='negotiate_client'),

   path('lafp3Home/', views.lafp3Home, name='lafp3Home'),

   path('blog/', views.blog, name='blog'),

   path('contact/', views.contact, name='contact'),

   path('profile/', views.profile, name='profile'),

   path('employee/', views.employee, name='employee'),

   path('application_form2/<int:CarLoanApplication_pk>/', views.application_form2, name='application_form2'),

   
   path('negotiated_amount_submit/<int:CarLoanApplication_pk>/', views.negotiated_amount_submit, name='negotiated_amount_submit'),
    
  path('update_amount/<int:CarLoanApplication_pk>/', views.update_amount, name='update_amount'),


   path('application_form2_nego/<int:CarLoanApplication_pk>/', views.application_form2_nego, name='application_form2_nego'),

   path('application_form/<int:CarLoanApplication_pk>/', views.application_form, name='application_form'),

   path('application_form_nego/<int:CarLoanApplication_pk>/', views.application_form_nego, name='application_form_nego'),

   path('application_list/', views.application_list, name='application_list'),

   path('nego_reject/<int:CarLoanApplication_pk>/',views.nego_reject,name='nego_reject'),

   path('form_reviewer_reject/<int:CarLoanApplication_pk>/', views.form_reviewer_reject, name='form_reviewer_reject'),

   path('crm_/',views.crm_,name='crm_'),

   path('crm_accept/<int:loan_account_id_pk>/',views.crm_accept, name='crm_accept'),

   path('crm_reject/<int:loan_account_id_pk>/', views.crm_reject,name='crm_reject'),

   path('single_post/', views.single_post, name='single_post'),

   path('login/', views.login, name='login'),

   path('about/', views.about, name='about'),

   path('services/', views.services, name='services'),
   
   path('apply/', views.apply, name='signin'),
   #path('', views.index, name='index'),
   path('test/', views.test, name='test'),
	# ex: /polls/5/
	path('<int:question_id>/', views.detail, name='detail'),
	# ex: /polls/5/results/
	path('<int:question_id>/results/', views.results, name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
	#path('login/', views.login, name='login'),
    path('show/', views.getUser, name='getUser'), 
    path('getApplication/<int:loan_account_id_pk>/', views.getApplication, name='getApplication'), 

    path('getReviewerHomePage/<int:loan_account_id_pk>/', views.getReviewerHomePage, name='getReviewerHomePage'), 

    path('index/', views.index, name='index'),
    path('showUpdate/<int:loan_account_id_pk>/', views.showUpdate, name='showUpdate'), 
    path('update/<int:loan_account_id_pk>/', views.update, name='update'), 

    url(r"^password-change$",PasswordChangeView.as_view(),name="password_change",),
    url(r"^password-change-done$",PasswordChangeDoneView.as_view(),name="password_change_done",),
    url(r"^password-reset/",PasswordResetView.as_view(template_name = 'reset_password.html', email_template_name = 'reset_password_email.html'),name="password_reset",),
    url(r"^password-reset-done",PasswordResetDoneView.as_view(template_name= 'reset_password_done.html'),name="password_reset_done",),
    url(r"^password-reset-complete",PasswordResetCompleteView.as_view(template_name = 'reset_password_complete.html'),
    name="password_reset_complete",),
    url(r"^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/",PasswordResetConfirmView.as_view(template_name= 'reset_password_confirm.html'),
    name="password_reset_confirm",),
]
