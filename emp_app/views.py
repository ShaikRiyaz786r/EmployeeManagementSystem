from django.shortcuts import render,redirect
from .models import Employee, Department, Role
from django.db.models import Q

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
    if request.method=='POST':
        firstname = request.POST.get('fn')
        lastname = request.POST.get('ln')
        department = request.POST.get('dept')
        role = request.POST.get('role')
        salary = request.POST.get('sal')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phn')
        hireDate = request.POST.get('hd')
        obj=Employee.objects.create(first_name=firstname,last_name=lastname,dept_id=department,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=hireDate)
        obj.save()
        return redirect('home')

    return render(request, 'add_emp.html')

def remove_emp(request):
    query_set = Employee.objects.all()
    context = {
        "query_set":query_set,
    }
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get("fln")
        dept = request.POST.get("dept")
        role = request.POST.get("role")
        emps = Employee.objects.all()
        if name:
            emps = Employee.objects.filter(Q(first_name__icontains = name)| Q(last_name__icontains=name))
        if dept:
            emps = Employee.objects.filter(dept__name = dept)
        if role:
            emps = Employee.objects.filter(role__name = role)
        context ={
            'emps':emps
        }
        return render(request,'view_emp.html',context)
    return render(request, 'filter_emp.html')

def delete(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('view_emp')

def update_emp(request,):
    query_set = Employee.objects.all()
    context = {
        "query_set":query_set,
    }
    return render(request,'update.html',context)

def update(request,pk):
    emp = Employee.objects.get(id=pk) #7
    context = {
        "emp":emp,
    }
    if request.method=='POST':
        firstname = request.POST.get('fn')
        lastname = request.POST.get('ln')
        salary = request.POST.get('sal')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phn')
        emp.first_name = firstname
        emp.last_name = lastname
        emp.salary = salary
        emp.bonus = bonus
        emp.phone = phone
        emp.save()
        return redirect('view_emp')
    return render(request,'update.html',context)