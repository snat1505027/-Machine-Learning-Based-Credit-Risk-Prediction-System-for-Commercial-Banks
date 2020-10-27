# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

from django.db.models.signals import post_save




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null = True, blank = True)
    sc = models.IntegerField(default=None, null = True, blank = True)
    def __str__(self):
        return self.question_text




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class UserPass(models.Model):
	userid = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	def __str__(self):
		return (self.userid+self.password)
		
class LoanType(models.Model):
	ltype =  models.CharField(max_length=50)
	def __str__(self):
		return self.ltype


class Branch(models.Model):
	branch_id = models.IntegerField(primary_key=True)
	branch_name = models.CharField(max_length=40, null = True, blank = True)
	branch_address = models.CharField(max_length=40, null = True, blank = True)


class Department(models.Model):
	department_id = models.IntegerField(primary_key=True)
	branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_id_dept')
	department_name = models.CharField(max_length=40, null = True, blank = True)


class AccountTable(models.Model):
	account_type = models.CharField(max_length=50)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
	fullName = models.CharField(max_length=100, null=True, blank=True)
	age = models.IntegerField(default=0)
	sex = models.CharField(max_length=10)
	marital_status = models.CharField(max_length=10)
	nominee_id = models.ForeignKey("self", on_delete=models.CASCADE, null = True, blank = True)
	balance = models.IntegerField(default=0)

	checking_account = models.IntegerField(default=0,null=True)
	savings_account = models.IntegerField(default=0,null=True)
	branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_id_acc', default=1)
	def __str__(self):
		str1=""	
		uname=""
		if self.nominee_id != None and self.nominee_id.user != None: 
			str1 = str(self.nominee_id.user.username)
		if self.user!= None:
			uname = self.user.username
		return (self.account_type + '\n' + uname + '\n' + '\n' + str(self.age) + '\n' + self.sex + '\n' + self.marital_status + '\n' + str(self.balance) + '\n' + str1 + '\n')




class Employee(models.Model):
	employee_id = models.IntegerField(primary_key=True)
	user_name = models.CharField(max_length=40, null = True, blank = True)
	department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_id_employee')
	employee_name = models.CharField(max_length=40, null = True, blank = True)
	age = models.IntegerField(default=0, null = True, blank = True)
	sex = models.CharField(max_length=10, null = True, blank = True)
	email = models.CharField(max_length=40, null = True, blank = True)
	address = models.CharField(max_length=40, null = True, blank = True)
	designation = models.CharField(max_length=40, null = True, blank = True)
	salary = models.IntegerField(default=0, null = True, blank = True)	
	account_id = models.ForeignKey(AccountTable, on_delete=models.CASCADE, related_name='acc_id_emp', blank = True, null=True)



class CarLoanData(models.Model):
	account_id = models.ForeignKey(AccountTable, on_delete=models.CASCADE, related_name='acc_id')
	monthly_income = models.IntegerField(default=0)
	monthly_expenditure = models.IntegerField(default=0)
	total_asset = models.IntegerField(default=0)
	car_price = models.IntegerField(default=0)
	requested_loan_amount = models.IntegerField(default=0)
	car_condition = models.CharField(max_length=20)
	car_vendor = models.CharField(max_length=20)
	car_brand = models.CharField(max_length=20)
	nominee_id = models.ForeignKey(AccountTable, on_delete=models.CASCADE, related_name='nom_id')	
	apply_date = models.DateTimeField(default=now, null = True, blank = True)

	checking_account = models.IntegerField(default=0,null=True)
	savings_account = models.IntegerField(default=0,null=True)
	duration = models.IntegerField(default=0,null=True)
	age =  models.IntegerField(default=0,null=True)
	sex = models.CharField(max_length=10,null=True)
	job = models.IntegerField(default=0,null=True)
	housing = models.CharField(max_length=20,null=True)

	def __str__(self):
		str1=""	
		if self.nominee_id != None and self.nominee_id.user != None: 
			str1 = '\nNominee: ' + str(self.nominee_id.user.username)
		return ( str(self.account_id) + '\nOwner\n' + 
			str(self.monthly_income) + '\n' + 
			str(self.monthly_expenditure) + '\n' +
			str(self.total_asset) + '\n' +
			str(self.car_price) + '\n' +  
			str(self.requested_loan_amount) + '\n' +
			self.car_condition + '\n' +
			self.car_vendor + '\n' +
			self.car_brand + '\n' + 
		 	str1 + '\n' +
		 	str(self.apply_date) + '\n')



from geoposition.fields import GeopositionField

class Zone(models.Model):
    name = models.CharField(max_length = 50 )
    kuerzel = models.CharField(max_length = 3 )
    kn_nr = models.CharField(max_length = 5 )
    beschreibung = models.CharField(max_length = 300 )
    adresse = models.CharField(max_length = 100 )
    position = GeopositionField()

class CarLoanApplication(models.Model):

	requested_loan_amount = models.IntegerField(null = True, blank = True)
	term = models.IntegerField(null = True, blank = True)
	apply_date = models.DateTimeField(default=now, null = True, blank = True)

	#personal information
	account_id = models.ForeignKey(AccountTable, on_delete=models.CASCADE, related_name='acc_id_application')
	first_name = models.CharField(max_length=40, null = True, blank = True)
	middle_name = models.CharField(max_length=40, null = True, blank = True)
	last_name = models.CharField(max_length=40, null = True, blank = True)
	date_of_birth = models.DateTimeField(null = True, blank = True)
	sex = models.CharField(max_length=10, null = True, blank = True)
	father = models.CharField(max_length=40, null = True, blank = True)
	mother = models.CharField(max_length=40, null = True, blank = True)
	nid = models.IntegerField(default=0,null = True, blank = True)
	passport = models.IntegerField(default=0, null = True, blank = True)



	#employement details
	profession = models.CharField(max_length=40, null = True, blank = True)


	organization_name = models.CharField(max_length=40, null = True, blank = True)
	office_address = models.CharField(max_length=40, null = True, blank = True)
	designation = models.CharField(max_length=40, null = True, blank = True)
	department = models.CharField(max_length=40, null = True, blank = True)
	division = models.CharField(max_length=40, null = True, blank = True)
	join_date = models.DateTimeField(null = True, blank = True)
	service_years = models.IntegerField(null = True, blank = True)
	employment_status = models.CharField(max_length=40, null = True, blank = True)
	salary_date = models.DateTimeField(null = True, blank = True)
	salary_payment_mode = models.CharField(max_length=40, null = True, blank = True)
	ownership_status = models.CharField(max_length=40, null = True, blank = True)
	share_holding_position = models.CharField(max_length=40, null = True, blank = True)
	business_starting_date = models.DateTimeField(null = True, blank = True)
	number_of_years_in_the_same_business = models.IntegerField(default=0,null = True, blank = True)
	number_of_employee = models.IntegerField(default=0, null = True, blank = True)

	industry_type = models.CharField(max_length=40, null = True, blank = True)
	main_product = models.CharField(max_length=40, null = True, blank = True)
	main_banker = models.CharField(max_length=40, null = True, blank = True)
	phone_no = models.CharField(max_length=40, null = True, blank = True)

	gross_salary = models.IntegerField(null = True, blank = True)
	net_salary = models.IntegerField(null = True, blank = True)
	business_income = models.IntegerField(null = True, blank = True)
	remmitance = models.IntegerField(null = True, blank = True)
	existing_rental_income = models.IntegerField(null = True, blank = True)

	address1 = models.CharField(max_length=40, null = True, blank = True)
	address2 = models.CharField(max_length=40, null = True, blank = True)
	address3 = models.CharField(max_length=40, null = True, blank = True)
	
	expected_rental_income = models.IntegerField(default=0, null = True, blank = True)
	interest_income = models.IntegerField(null = True, blank = True)


	other_income = models.CharField(max_length=40, null = True, blank = True)
	
	other_income_1 = models.CharField(max_length=40, null = True, blank = True)
	other_income_2 = models.CharField(max_length=40, null = True, blank = True)

	total_income = models.IntegerField(null = True, blank = True)

	house_rent = models.IntegerField(null = True, blank = True)
	utilities_bill = models.IntegerField(null = True, blank = True)
	bank_loan_emi = models.IntegerField(null = True, blank = True)
	other_banks_loan_emi = models.IntegerField(null = True, blank = True)
	credit_card_performance = models.FloatField(null = True, blank = True)
	total_expense = models.IntegerField(null = True, blank = True)

	applied_loan_amount = models.IntegerField(null = True, blank = True)
	lterm = models.CharField(max_length=40, null = True, blank = True)
	preferred_emi_amount = models.IntegerField(null = True, blank = True)
	preferred_emi_date = models.DateTimeField(null = True, blank = True)
	benefitiary_pay_date = models.DateTimeField(null = True, blank = True)

	car_price = models.IntegerField(null = True, blank = True)
	equity_paid = models.IntegerField(null = True, blank = True, default = 0)
	registration_cost = models.IntegerField(null = True, blank = True)
	remaining_equity_to_be_paid = models.IntegerField(null = True, blank = True)
	total_required_loan_amount = models.IntegerField(null = True, blank = True)

	car_vendor = models.CharField(max_length=20, null = True, blank = True)
	car_vendor_address = models.CharField(max_length = 40, null = True, blank = True)
	car_vendor_phone_no = models.CharField(max_length = 40, null = True, blank = True)

	car_condition = models.CharField(max_length=20, null = True, blank = True)
	car_brand = models.CharField(max_length=20,null = True, blank = True)
	car_model = models.CharField(max_length=20,null = True, blank = True)
	cc = models.IntegerField(default=0,null = True, blank = True)
	manufacturing_year = models.DateTimeField(null = True, blank = True)
	country_of_origin = models.CharField(max_length=20,null = True, blank = True)
	color = models.CharField(max_length=20,null = True, blank = True)
	chasis_number = models.CharField(max_length=40,null = True, blank = True)
	engine_number = models.CharField(max_length=40,null = True, blank = True)
	registration_number = models.CharField(max_length=40,null = True, blank = True)
	review_status = models.CharField(max_length=40,null = True, blank = True)
	negotiated_amount = models.IntegerField(default=0,null=True,blank=True)
	prediction = models.FloatField(default=0,null=True,blank=True)
	#ML input
	job = models.IntegerField(default=0,null=True)
	housing = models.CharField(max_length=20,null=True)
	
	def __str__(self):
		str1= str(self.requested_loan_amount) + " " + self.first_name
		return str1;	
#cc = CarLoanData(account_id=1, monthly_income = 20000, monthly_expenditure = 5000, total_asset = 100000, car_price = 800000, requested_loan_amount = 500000, car_condition = "old", car_vendor = "type1", car_brand="toyota")
#from polls.models import AccountTable, CarLoanData


class Negotiator_CRM(models.Model):
	application_id = models.ForeignKey(CarLoanApplication, on_delete=models.CASCADE, related_name='application_id_nego', null = True, blank = True)
	negotiated_amount = models.IntegerField(default=0, null=True, blank=True)
	negotiated_status = models.CharField(max_length=100, null=True, blank=True)
	crm_status = models.CharField(max_length=100, null=True, blank=True)

class CarLoanData2(models.Model):
	account_id = models.ForeignKey(AccountTable, on_delete=models.CASCADE, related_name='acc_id2')
	application_id = models.ForeignKey(CarLoanApplication,on_delete=models.CASCADE,related_name='app_id')
	requested_loan_amount = models.IntegerField(default=0)
	purpose = models.CharField(max_length=40,null=True)
	checking_account = models.IntegerField(default=0,null=True)
	savings_account = models.IntegerField(default=0,null=True)
	duration = models.IntegerField(default=0,null=True)
	age =  models.IntegerField(default=0,null=True)
	sex = models.CharField(max_length=10,null=True)
	job = models.IntegerField(default=0,null=True)
	housing = models.CharField(max_length=20,null=True)
	risk = models.CharField(max_length=20,null=True)

	def __str__(self):
		str1=""	
		return ( str(self.account_id) + '\n' + 
			str(self.application_id) + '\n' + 
			self.purpose + '\n' +
			str(self.requested_loan_amount) + '\n' +
			str(self.checking_account) + '\n' +  
			str(self.savings_account) + '\n' +
			str(self.duration) + '\n' +
			str(self.age) + '\n' +
			self.sex + '\n' + 
		 	str(self.job) + '\n' +
		 	self.housing + '\n' )
			#self.risk+'\n')



class CSVReader(models.Model):
	account_id =  models.ForeignKey(AccountTable,on_delete=models.CASCADE,null=True, blank=True)
	upload = models.FileField(upload_to='uploads/', null = True, blank=True, max_length=100000)
	apply_date = models.DateTimeField(default=now, null = True, blank = True) 
	negotiated_amount = models.IntegerField(default=0, null=True, blank=True)
	prediction = models.FloatField(default=0,null=True,blank=True)
	allowable_amount =  models.IntegerField(default=0, null=True, blank=True)
	status = models.CharField(max_length=40,null = True, blank = True)

	def __str__(self):
		str1=""	
		return ( str(self.id) + '\n' + 
			str(self.status) + '\n' +
			str(self.pk) + '\n' +
			str(self.prediction) + '\n')



