from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import EmployeeAccountTable, Employee
from polls.models import CarLoanApplication, CSVReader, AccountTable
from django.contrib.auth.models import User
import pickle
import category_encoders as ce
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import csv


# def index(request):
#     context = {}
#     template = loader.get_template('employee/login.html')
#     return HttpResponse(template.render(context, request))


def tempChart(request):
    """
    Displays all the graphs regarding loan distribution. 

    Optional attributes:
        | ``user``: valid employee from Employee table
        | ``context``: holds the employee object from the Employee table

    """
    user = Employee.objects.get(user_name=request.user.username)
    context = {
        'user_acc': user,
    }
    return render(request, 'employee/tempChart.html', context)

def defaulter(request):
    """
    Displays all the graphs regarding defaulter. 

    Optional attributes:
        | ``user``: valid employee from Employee table
        | ``context``: holds the employee object from the Employee table

    """
    user = Employee.objects.get(user_name=request.user.username)
    context = {
        'user_acc': user,
    }
    return render(request, 'employee/defaulter.html', context)

def interestRate(request):
    """
    Displays all the graphs regarding interest rate. 

    Optional attributes:
        | ``user``: valid employee from Employee table
        | ``context``: holds the employee object from the Employee table

    """
    user = Employee.objects.get(user_name=request.user.username)
    context = {
        'user_acc': user,
    }
    return render(request, 'employee/interest_rate.html', context)


def profile(request):
    user = Employee.objects.get(user_name=request.user.username)
    context = {
        'user_acc': user,
    }
    return render(request, 'employee/profile_emp.html', context)


def FRList(request):
    """
    Displays list of loan applications to the Form Reviewer's homepage that has been submitted by the clients but has not been reviewed yet.

    Optional attributes:
        | ``loan``: all objects of CSVReader i.e. all the loan applications
        | ``context``: holds the employee object from the Employee table and all loan appliactions from the CSVReader table that will be passed to the template
        | ``user``: valid employee from Employee table
        | ``template_name``: the name of the template to use

    """
    loan = CSVReader.objects.all()
    user = Employee.objects.get(user_name=request.user.username)
    template_name = 'employee/application_list_rev.html'
    if(user.designation != "Form Reviewer"):
        loan = None
    context = {
        'loan': loan,
        'user_acc': user,
    }
    return render(request,'employee/application_list_rev.html',context)

def dashboard(request):
    """
    Displays the employee home page if it is a valid employee otherwise displays the login page. 

    Optional attributes:
        | ``template_name``: the name of the template to use
        | ``context``: holds the employee object from the database that will be passed to the template
        | ``user``: valid user from User table
        | ``user_list``: employee list from Employee table

    """
    template_name = 'employee/login.html'
    context = None
    if(request.user.username != ""):
        user = User.objects.get(username=request.user.username)     
        user_list = Employee.objects.all()
        for ul in user_list:
            if(ul.user_name == request.user.username):
                template_name = 'employee/profile_emp.html'
                context = {
                    'user_acc': ul,
                }
                request.session['FLAG'] = True
                break
    return render(request, template_name, context)


def NList(request):
    """
    Displays list of loan applications to Negotiators' homepage that has been reviewed by the Form Reviewer but has not been negotiated yet.

    Optional attributes:
        | ``loan``: all objects of CSVReader i.e. all the loan applications
        | ``user``: valid employee from Employee table
        | ``loan_am``: stores all the requested loan amount from all the loan applications
        | ``mylist``: zips all the loan applications and their corresponding requested loan amount
        | ``context``: holds the employee object from the Employee table and mylist

    """
    loan = CSVReader.objects.all()
    user = Employee.objects.get(user_name=request.user.username)
    import csv
    loan_am = []
    for ll in loan:
        df = pd.read_csv(ll.upload, skipinitialspace=True)
        print("loan amount:")
        temp_list = df.to_dict('list')

        # temp = temp['loan_amount'][0]
        print(temp_list['loan_amount'][0])
        loan_am.append(temp_list['loan_amount'][0])



    mylist = zip(loan,loan_am)
    if(user.designation != "Negotiator"):
        loan = None
    context = {
        'loan': mylist,
        'user_acc': user,
    }
    return render(request,'employee/application_list_nego.html',context)


def ATables(request):
    """
    Displays list of clients' accounts from the AccountTable data table.

    Optional attributes:
        | ``accounts``: all objects of AccountTable i.e. all the accounts of the bank.
        | ``context``: holds the employee object from the Employee table and all account objects from the AccountTable table that will be passed to the template
        | ``user``: valid employee from Employee table

    """
    accounts = AccountTable.objects.all()
    user = Employee.objects.get(user_name=request.user.username)

    context = {
        'accounts': accounts,
        'user_acc': user,
    }
    return render(request,'employee/account_tables.html',context)


def LHistory(request):
    """
    Displays loan history/list of loan applications that has been accepted or rejected in the past.

    Optional attributes:
        | ``loan_hist``: all objects of CSVReader i.e. all the loan applications
        | ``user``: valid employee from Employee table
        | ``context``: holds the employee object from the Employee table and all objects of CSVReader

    """
    user = Employee.objects.get(user_name=request.user.username)
    loan_hist = CSVReader.objects.all()

    context = {
        'loan_hist': loan_hist,
        'user_acc': user,
    }
    return render(request,'employee/loan_history.html',context)

   
def logout_emp(request):
    try:
        del request.session["MEM_ID"]
    except KeyError:
        pass


def form_reviewer_reject(request,CarLoanApplication_pk):
    loanee = CSVReader.objects.get(pk=CarLoanApplication_pk)
    
    print(loanee)

    loanee.status = "REJECTED_REV"
    loanee.save()
    # for r in loanee:
    #     r.delete()
    
    return redirect("FRList")


def update_amount(request, CarLoanApplication_pk):
    """
    Displays a modal to take input(negotiated amount for loan) from the Negotiator and updates the negotiated_amount field in that loan application object and redirects to Negotiator homepage.

    Optional attributes:
        | ``loan``: specific loan application from CSVReader
        | ``nego_amount``: stores negotiated amount that has been submitted by Negotiator

    """
    loan = CSVReader.objects.get(pk = CarLoanApplication_pk)
    nego_amount = request.POST["update_amount"]
    loan.status = "NEGOTIATED"
    loan.negotiated_amount=int(nego_amount)
    loan.save()
    return redirect("NList")
    

def getCSV(request, loan_id):
    """
    Displays the whole loan application to the employee(i.e., Form Reviewer, Negotiator, CRM) for further analysis.

    Optional attributes:
        | ``file_name``: specific loan application from CSVReader
        | ``user``: valid employee from Employee table
        | ``df``: read the loan application(which is in CSV format) in pandas dataframe format
        | ``temp_list``: convert from pandas dataframe to list
        | ``context``: holds the employee object from the Employee table and temp_list

    """
    file_name = CSVReader.objects.get(pk=loan_id)
    user = Employee.objects.get(user_name=request.user.username)
    df = pd.read_csv(file_name.upload, skipinitialspace=True)
    temp_list = df.to_dict('list')
    if(user.designation != "Form Reviewer"):
        df = None

    context = {
        'loan_app': temp_list,
        'user_acc': user,
    }
    return render(request,'employee/form_wizards2.html',context)


def CRMList(request):
    """
    Displays list of loan applications to the Client Relation Manager's homepage that has been reviewed by the Form Reviewer and negotiated by the Negotiator but has not been confirmed yet.

    Optional attributes:
        | ``loan``: all objects of CSVReader i.e. all the loan applications
        | ``user``: valid employee from Employee table
        | ``loan_am``: stores all the requested loan amount from all the loan applications
        | ``mylist``: zips all the loan applications and their corresponding requested loan amount
        | ``context``: holds the employee object from the Employee table and mylist

    """
    loan = CSVReader.objects.all()
    user = Employee.objects.get(user_name=request.user.username)

    import csv
    loan_am = []
    for ll in loan:
        df = pd.read_csv(ll.upload, skipinitialspace=True)
        temp_list = df.to_dict('list')
        loan_am.append(temp_list['loan_amount'][0])


    mylist = zip(loan,loan_am)
    if(user.designation != "CRM"):
        loan = None
    context = {
        'loan': mylist,
        'user_acc': user,
    }
    return render(request,'employee/crm_application_list.html',context)


def generatePrediction(request, loan_id):
    
    file_name = CSVReader.objects.get(pk=loan_id)

    df = pd.read_csv(file_name.upload)
    df.drop(df.columns[0],axis=1,inplace=True)
    

    pkl_filename = "pickle_model.pkl"

    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
        
    import numpy as np
    ohe = ce.OneHotEncoder(handle_unknown='ignore', use_cat_names=True)
    X_trains = pd.read_pickle("strict_train.pkl")
    X_tests = pd.read_pickle("test_dataset.pkl")
    X_t = df.copy()
    #X_t = pd.read_pickle("case1.pkl")
    X_t.index = {len(X_tests)}
    X_tests.append(X_t)
    X_train_ohe = ohe.fit_transform(X_trains)
    #X_test_ohe = ohe.transform(X_tests)
    X_test_ohe = ohe.transform(X_t)
    X_test_ohe = X_test_ohe.fillna(0)
    X_test_ohe.to_pickle("ohe_test.pkl")
    Ypredict = pickle_model.predict_proba(X_test_ohe)
    print(Ypredict)

    print("For one")

    np.save('predictions_2.npy', Ypredict) # save
    new_num_arr = np.load('predictions_2.npy') # load
    #b = Ypredict[X_t.index-1]
    # print(b[0][1])
    # temp.prediction = b[0][1]
    # temp.save()
    
    print(Ypredict[0][1])
    file_name.prediction = Ypredict[0][1]
    file_name.status = "REVIEWED"

    print("loan amount:")
    temp_list = df.to_dict('list')

        # temp = temp['loan_amount'][0]
    print(temp_list['loan_amount'][0])
    
    
    file_name.allowable_amount = Ypredict[0][1] * temp_list['loan_amount'][0]
    file_name.save()

    loan = CSVReader.objects.all()
    user = Employee.objects.get(user_name=request.user.username)
    template_name = 'application_list.html'
    print(user.designation)

    
    if(user.designation != "Form Reviewer"):
        loan = None
    context = {
        'loan': loan,

    }
    return redirect("FRList")
    #return render(request,'application_list.html',context)


def crm_accept(request, loan_account_id_pk):
    loan = CSVReader.objects.get(pk=loan_account_id_pk)
    loan.status="ACCEPTED"
    loan.save()
    
    user = Employee.objects.get(user_name=request.user.username)
    account = AccountTable.objects.get(id=loan.account_id.pk)
    user_client = User.objects.get(id=account.user.pk)

    print(user_client.email)
    
    #EMAIL
    # create message object instance
    msg = MIMEMultipart()

    message = "Congratulations! Your loan application has been approved."
     
    # setup the parameters of the message
    password = "tiderc272107"
    msg['From'] = "creditbankcse408@gmail.com"
    msg['To'] = user_client.email
    msg['Subject'] = "Confirmation of Loan Grant"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com: 587')
     
    server.starttls()
    server.login(msg['From'], password) 
    server.sendmail(msg['From'], msg['To'], msg.as_string()) 
    server.quit()
    return redirect("CRMList")



def nego_reject(request,CarLoanApplication_pk):
    loanee = CSVReader.objects.get(pk=CarLoanApplication_pk)
    loanee.status="REJECTED_NEGO"
    loanee.save()
    
    return redirect("NList")



def crm_reject(request,loan_account_id_pk):
    loan = CSVReader.objects.get(pk=loan_account_id_pk)
    loan.status="REJECTED_CRM"
    loan.save()

    user = Employee.objects.get(user_name=request.user.username)
    print("Here in CRM_REJECT")
    
    account = AccountTable.objects.get(id=loan.account_id.pk)
    user_client = User.objects.get(id=account.user.pk)
    print(user_client)
    print(user_client.email)

    #EMAIL
    # create message object instance
    
    msg = MIMEMultipart()

    message = "Sorry! Your loan application could not be approved."
     
    # setup the parameters of the message
    password = "tiderc272107"
    msg['From'] = "creditbankcse408@gmail.com"
    msg['To'] = user_client.email
    msg['Subject'] = "Notification of Loan Rejection"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
     
    server.starttls()
     
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
     
     
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
     
    print("email sent")
    
    
    
    print(user.designation)
    
    return redirect("CRMList")
