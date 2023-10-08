from django.shortcuts import render,redirect
from .models import *
def insert_home_page(request):
    return render(request,"font/home_page.html")

def upload_home_data(request):
    if request.method=="POST":
        user_name=request.POST['name']
        user_email=request.POST['email']
        user_contact=request.POST['contact']
        user_password=request.POST['password']
        user_data=Student.objects.create(Name=user_name,Email=user_email,Contact=user_contact,Password=user_password)
        user_data.save()
        return redirect("fetch")
    
def fetch_data_page(request):
    all_data=Student.objects.all()
    return render(request,"font/fetch_data.html",{'key1':all_data})

def edit_page(request,pk):
    particular_data=Student.objects.get(id=pk)
    return render(request,"font/edit.html",{'key2':particular_data})

def edit_upload_page(request,pk):
    update_data=Student.objects.get(id=pk)
    update_data.Name=request.POST['name']
    update_data.Email=request.POST['email']
    update_data.Contact=request.POST['contact']
    update_data.Password=request.POST['password']
    update_data.save()
    return redirect('fetch')

def edit_delete_page(request,pk):
    delete_data=Student.objects.get(id=pk)
    delete_data.delete()
    return redirect("fetch")



