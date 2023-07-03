from django.shortcuts import render, redirect
from employees.models import employees

def home(request):
    emp=employees.objects.all()
    context={
        'emp':emp
    }
    return render(request,'index.html',context)

def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp=employees(
            name=name,
            email=email,
            address=address,
            phone=phone
        )

        emp.save()   
        return redirect('/')       
    return render(request,'create.html')

def edit(request):
    return render(request,'edit.html')