# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.core.files.base import File

from .models import Question, Choice, LoanType, Zone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from polls.forms import (
    RegistrationForm,
    EditProfileForm
)
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
import pandas as pd

from django.urls import reverse

from django.shortcuts import get_object_or_404, render

from .models import Choice, Question, CarLoanData, AccountTable, CarLoanApplication, Employee, Negotiator_CRM,CarLoanData2, CSVReader
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from django.shortcuts import render_to_response, get_object_or_404, redirect

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
from django.views.decorators.csrf import csrf_exempt
from polls.models import CarLoanData, AccountTable, CarLoanApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib





carloandict = {}
carloandict2 = {}
formrev_carloan = {}

@csrf_exempt
def handleForm(request):    
    carloandict2['loan_amount'] = request.POST['loan_amount']
    carloandict2['term'] = request.POST['term']
    carloandict2['interest_rate'] = request.POST['interest_rate']
    carloandict2['installment'] = request.POST['installment']
    carloandict2['grade'] = request.POST['grade']
    carloandict2['home_ownership'] = request.POST['home_ownership']
    carloandict2['annual_income'] = request.POST['annual_income']
    carloandict2['verification_status'] = 'Source Verified'
    carloandict2['pymnt_plan'] = 'n'
    carloandict2['purpose'] = request.POST['purpose']
    carloandict2['addr_state'] = request.POST['addr_state']
    carloandict2['dti'] = '16.89'
    carloandict2['delinq_2yrs'] = request.POST['delinq_2yrs']
    carloandict2['inq_last_6mths'] = request.POST['inq_last_6mths']
    carloandict2['mths_since_last_delinq'] = request.POST['mths_since_last_delinq']
    carloandict2['mths_since_last_record'] = request.POST['mths_since_last_record']
    carloandict2['open_acc'] = request.POST['open_acc']
    carloandict2['pub_rec'] = request.POST['pub_rec']
    carloandict2['revol_bal'] = request.POST['revol_bal']
    carloandict2['revol_util'] = request.POST['revol_util']
    carloandict2['total_acc'] = request.POST['total_acc']
    carloandict2['open_act_il'] = request.POST['open_act_il']
    carloandict2['acc_open_past_24mths'] = request.POST['acc_open_past_24mths']
    carloandict2['avg_cur_bal'] = request.POST['avg_cur_bal']
    carloandict2['bc_open_to_buy'] = request.POST['bc_open_to_buy']
    carloandict2['bc_util'] = request.POST['bc_util']
    carloandict2['chargeoff_within_12_mths'] = request.POST['chargeoff_within_12_mths']
    carloandict2['delinq_amnt'] = request.POST['delinq_amnt']
    carloandict2['mo_sin_old_il_acct'] = request.POST['mo_sin_old_il_acct']
    carloandict2['mo_sin_old_rev_tl_op'] = request.POST['mo_sin_old_rev_tl_op']
    carloandict2['mo_sin_rcnt_rev_tl_op'] = request.POST['mo_sin_rcnt_rev_tl_op']
    carloandict2['mo_sin_rcnt_tl'] = request.POST['mo_sin_rcnt_tl']
    carloandict2['mort_acc'] = request.POST['mort_acc']
    carloandict2['mths_since_recent_bc'] = request.POST['mths_since_recent_bc']
    carloandict2['mths_since_recent_bc_dlq'] = request.POST['mths_since_recent_bc_dlq']
    carloandict2['mths_since_recent_inq'] = request.POST['mths_since_recent_inq']
    carloandict2['mths_since_recent_revol_delinq'] = request.POST['mths_since_recent_revol_delinq']
    carloandict2['num_accts_ever_120_pd'] = request.POST['num_accts_ever_120_pd']
    carloandict2['num_actv_bc_tl'] = request.POST['num_actv_bc_tl']
    carloandict2['num_actv_rev_tl'] = request.POST['num_actv_rev_tl']
    carloandict2['num_bc_sats'] = request.POST['num_bc_sats']
    carloandict2['num_bc_tl'] = request.POST['num_bc_tl']
    carloandict2['num_il_tl'] = request.POST['num_il_tl']
    carloandict2['num_op_rev_tl'] = request.POST['num_op_rev_tl']
    carloandict2['num_rev_accts'] = request.POST['num_rev_accts']
    #from tisha
    carloandict2['num_rev_tl_bal_gt_0'] = request.POST['num_rev_tl_bal_gt_0']
    carloandict2['num_sats'] = request.POST['num_sats']
    carloandict2['num_tl_120dpd_2m'] = request.POST['num_tl_120dpd_2m']
    carloandict2['num_tl_30dpd'] = request.POST['num_tl_30dpd']
    carloandict2['num_tl_90g_dpd_24m'] = request.POST['num_tl_90g_dpd_24m']
    carloandict2['num_tl_op_past_12m'] = request.POST['num_tl_op_past_12m']
    carloandict2['pct_tl_nvr_dlq'] = request.POST['pct_tl_nvr_dlq']
    carloandict2['percent_bc_gt_75'] = request.POST['percent_bc_gt_75']
    carloandict2['pub_rec_bankruptcies'] = request.POST['pub_rec_bankruptcies']
    carloandict2['tax_liens'] = request.POST['tax_liens']
    carloandict2['tot_hi_cred_lim'] = request.POST['tot_hi_cred_lim']
    carloandict2['total_bal_ex_mort'] = request.POST['total_bal_ex_mort']
    carloandict2['total_bc_limit'] = request.POST['total_bc_limit']
    carloandict2['total_il_high_credit_limit'] = request.POST['total_il_high_credit_limit']
    carloandict2['revol_bal_joint'] = request.POST['revol_bal_joint']
    
    carloandict2['sec_app_earliest_cr_line'] = request.POST['sec_app_earliest_cr_line']
    carloandict2['sec_app_inq_last_6mths'] = request.POST['sec_app_inq_last_6mths']
    carloandict2['sec_app_mort_acc'] = request.POST['sec_app_mort_acc']
    carloandict2['sec_app_open_acc'] = request.POST['sec_app_open_acc']
    carloandict2['sec_app_revol_util'] = request.POST['sec_app_revol_util']
    carloandict2['sec_app_open_act_il'] = request.POST['sec_app_open_act_il']
    carloandict2['sec_app_num_rev_accts'] = request.POST['sec_app_num_rev_accts']
    carloandict2['sec_app_chargeoff_within_12_mths'] = request.POST['sec_app_chargeoff_within_12_mths']
    carloandict2['sec_app_collections_12_mths_ex_med'] = request.POST['sec_app_collections_12_mths_ex_med']
    carloandict2['sec_app_mths_since_last_major_derog'] = request.POST['sec_app_mths_since_last_major_derog']
     
    carloandict2['hardship_flag'] = request.POST['hardship_flag']
    carloandict2['hardship_type'] = request.POST['hardship_type']
    carloandict2['hardship_reason'] = request.POST['hardship_reason']
    carloandict2['hardship_status'] = request.POST['hardship_status']

    carloandict2['deferral_term'] = request.POST['deferral_term']
    carloandict2['hardship_amount'] = request.POST['hardship_amount']
    carloandict2['hardship_start_date'] = request.POST['hardship_start_date']
    carloandict2['hardship_end_date'] = request.POST['hardship_end_date']
    carloandict2['payment_plan_start_date'] = request.POST['payment_plan_start_date']
    carloandict2['hardship_length'] = request.POST['hardship_length']
    carloandict2['hardship_dpd'] = request.POST['hardship_dpd']
    carloandict2['hardship_loan_status'] = request.POST['hardship_loan_status']
    carloandict2['orig_projected_additional_accrued_interest'] = request.POST['orig_projected_additional_accrued_interest']
    carloandict2['hardship_payoff_balance_amount'] = request.POST['hardship_payoff_balance_amount']
    carloandict2['hardship_last_payment_amount'] = request.POST['hardship_last_payment_amount']
    carloandict2['disbursement_method'] = request.POST['disbursement_method']
    carloandict2['debt_settlement_flag'] = request.POST['debt_settlement_flag']
    carloandict2['debt_settlement_flag_date'] = request.POST['debt_settlement_flag_date']
    carloandict2['settlement_status'] = request.POST['settlement_status']
    carloandict2['settlement_date'] = request.POST['settlement_date']
    carloandict2['settlement_amount'] = request.POST['settlement_amount']
    carloandict2['settlement_percentage'] = request.POST['settlement_percentage']
    carloandict2['settlement_term'] = request.POST['settlement_term']
    
    print(carloandict2)
    print(' hah hahahhahha hahhhaha ')
    tree = CSVReader.objects.latest('id')  
    print(tree.pk)  

    df = pd.DataFrame([carloandict2])
    
    file_name = "/home/tisha/Documents/Past_files/Documents/Bristy/Safer/Merged_renamedjs/ISD_4-1___/mysite/media/uploads/"+str(tree.pk)+".csv"
    #file_name = "/home/tisha/Documents/Past_files/Documents/Bristy/Safer/ISD_4-1/mysite/media/uploads/"+str(tree.pk)+".csv"
    

    df.to_csv(file_name)
    print(df)
    tdf = pd.read_csv(file_name)
    print(tdf)
    f = open(file_name, 'rb')
    content = File(f)
    account = AccountTable.objects.get(user = request.user)
    entry = CSVReader(account_id=account,negotiated_amount=None, prediction=None,allowable_amount = None, status = "APPLIED")
    entry.save()
    ct = CSVReader.objects.latest('id')  
    ct.upload.save(file_name, content, True)
    print(ct.apply_date,ct.pk, ct.account_id.user.username)
    return render(request, 'NewHomepage/contact.html', context=None)
    



def profile(request):
    if request.user.username != "":
        user_ = User.objects.get(username=request.user.username)
        #user_acc = None
        if(AccountTable.objects.filter(user = user_).exists()):
           user_acc = AccountTable.objects.get(user = user_)
           tag = "user"
           context = {
               'user_acc':user_acc,
               'tag': tag
           }
        else:
           user_acc = Employee.objects.get(user_name = user_)
           tag = "employee"
           context = {
               'user_acc':user_acc,
               'tag': tag
           }
            #print("Nai")
        #return render(request, 'profile.html', context=None)
        return render(request, 'profile.html', context=context)
    else:
        return render(request, 'profile.html', context=None)



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


def convert(val):
    if(val != ""):
        val = int(val)
    else:
        val = None
    return val

def convert_f(val):
    if(val != ""):
        val = float(val)
    else:
        val = None
    return val



def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if(request.user.username != "" ):
        user = User.objects.get(username=request.user.username)
        #print(user)
        user_list = Employee.objects.all()
        for ul in user_list:
            if(ul.user_name == request.user.username):
                print("exists in employee")
                return redirect("dashboard")
        user_list = AccountTable.objects.all()
        for ul in user_list:
            if ul.user == user:
                print("exists in user")
                return redirect("home")



def homepage(request):
    verified = 0
    template_name = 'NewHomepage/index.html'
    
    if(request.user.username != "" ):
        user = User.objects.get(username=request.user.username)
        #print(user)
        user_list = AccountTable.objects.all()
        for ul in user_list:
            if ul.user == user:
                print("exists in user")
                break

    context = {
        'verified' : verified
    }
    
    return render(request,template_name,context)


def about(request):
    return render(request,'NewHomepage/about.html',context=None)


def services(request):
    return render(request,'NewHomepage/services.html',context=None)


def verification(request):
    verified = 1
    context = {
        'verified' : verified
    }
    return render(request,'NewHomepage/index.html',context)


def apply(request):
    """
    Redirects users based on whether they are in the admins group
    """
    return render(request,'index.html',context=None)


def index(request):

    user_list = AccountTable.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, 'login.html', context)



def login(request):
	return render(request,'signin.html',context=None)










