# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, AccountTable, LoanType, CarLoanData, CarLoanData2,UserPass, Profile, CarLoanApplication, Branch, Department, Employee, Negotiator_CRM, CSVReader

admin.site.register(Question)
admin.site.register(AccountTable)
admin.site.register(CarLoanData)
admin.site.register(UserPass)
admin.site.register(Profile)
admin.site.register(CarLoanApplication)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Negotiator_CRM)
admin.site.register(CarLoanData2)
admin.site.register(CSVReader)
admin.site.register(LoanType)