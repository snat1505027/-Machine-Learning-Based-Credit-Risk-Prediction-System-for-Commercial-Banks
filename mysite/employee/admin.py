from django.contrib import admin

# Register your models here.
from .models import Department, EmployeeAccountTable, Branch, Employee


admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(EmployeeAccountTable)
admin.site.register(Employee)
