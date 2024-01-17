from django.shortcuts import render
from .models import Employee, Department, Role

def home(request):
    return render(request, 'index.html')

def view_emp(request):
    employees = Employee.objects.all()
    for i in employees:
        print(i.first_name)
    context={
        'emps':employees,
    }
    return render(request, 'view_emp.html',context)

def add_emp(request):
    return render(request, 'add_emp.html')

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')