from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def create(request):
    return render(request,'create.html')

def edit(request):
    return render(request,'edit.html')