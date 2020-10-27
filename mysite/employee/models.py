from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



# Create your models here.

class Branch(models.Model):
	branch_id = models.IntegerField(primary_key=True)
	branch_name = models.CharField(max_length=40, null = True, blank = True)
	branch_address = models.CharField(max_length=40, null = True, blank = True)


class Department(models.Model):
	department_id = models.IntegerField(primary_key=True)
	branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_id_dept_emp')
	department_name = models.CharField(max_length=40, null = True, blank = True)



class EmployeeAccountTable(models.Model):
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
	branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_id_acc_emp', default=1)
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
	department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_id_employee_emp')
	employee_name = models.CharField(max_length=40, null = True, blank = True)
	age = models.IntegerField(default=0, null = True, blank = True)
	sex = models.CharField(max_length=10, null = True, blank = True)
	email = models.CharField(max_length=40, null = True, blank = True)
	address = models.CharField(max_length=40, null = True, blank = True)
	designation = models.CharField(max_length=40, null = True, blank = True)
	salary = models.IntegerField(default=0, null = True, blank = True)	
	account_id = models.ForeignKey(EmployeeAccountTable, on_delete=models.CASCADE, related_name='acc_id_emp_emp', blank = True, null=True)
