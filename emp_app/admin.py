from django.contrib import admin
from . models import Department,Role,Employee

class DepartmentModel(admin.ModelAdmin):
    list_display = ['name','location']
class RoleModel(admin.ModelAdmin):
    list_display = ['name']
class EmployeeModel(admin.ModelAdmin):
    list_display=["first_name","last_name",'dept','salary','bonus','role','phone','hire_date']

admin.site.register(Department,DepartmentModel)
admin.site.register(Role,RoleModel)
admin.site.register(Employee,EmployeeModel)
