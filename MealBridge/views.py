from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as ln,logout as lo
from django.contrib.auth.decorators import login_required
from core.models import VendorData,Feedback,VendorData_bennett,VendorData_Dtu,VendorData_sharda,VendorData_Galgotia

@login_required(login_url='login')
def home(request):
    if request.method=="POST":
        u_name=request.POST.get('name')
        u_email=request.POST.get('email')
        u_sn=request.POST.get('shop-name')
        u_info=request.POST.get('other-info')
        u_college=request.POST.get('cname')
        if u_college=='BU':
            vendor = VendorData_bennett.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor.save()
            vendor1 = VendorData.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor1.save()
        if u_college=='GU':
            vendor = VendorData_Galgotia.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor.save()
            vendor1 = VendorData.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor1.save()
        if u_college=='SU':
            vendor = VendorData_sharda.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor.save()
            vendor1 = VendorData.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor1.save()
        if u_college=='DTU':
            vendor = VendorData_Dtu.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor.save()
            vendor1 = VendorData.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor1.save()
        else :
            vendor1 = VendorData.objects.create(name=u_name,email=u_email,shop_name=u_sn,info=u_info)
            vendor1.save()
        print(u_college)
    return render(request ,"index.html")

def login(request):
    if request.method=="POST":
        u_name=request.POST.get('username')
        pass1=request.POST.get('password')
        user = authenticate(request,username=u_name,password=pass1)
        if user is not None:
            ln(request,user)
            return redirect('home')
        else:
            return HttpResponse("wrong info")
    return render(request ,"login.html")

def signup(request):
    if request.method=='POST':
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('confirm-password')
        if password==c_password:
             
             my_user=User.objects.create_user(u_name,email,password)
             my_user.save()
        else:
            return HttpResponse("password donot match")

       
        return redirect('login')
        

    return render(request ,"signup.html")
def logoutPage(request):
    lo(request)
    return redirect('login')
def contact(request):
    if request.method=='POST':
        u_name= request.POST.get('name')
        u_email= request.POST.get('email')
        info=request.POST.get('message')
        feed = Feedback.objects.create(name=u_name,email=u_email,info=info)
        feed.save()
        return HttpResponse("Thanks for your feedback")
    return render(request,'contact.html')
def aboutus(request):
    return render(request,"about.html")
def vd(request):
    queryset = VendorData.objects.all()
    
    # Prepare a list to store data (or process it as needed)
    data = []
    for obj in queryset.iterator():  # Efficiently fetch one record at a time
        data.append(obj)  # Add each object to the data list
    return render(request, 'tiffin.html', {'data': data})
def vdb(request):
    queryset = VendorData_bennett.objects.all()
    
    # Prepare a list to store data (or process it as needed)
    data = []
    for obj in queryset.iterator():  # Efficiently fetch one record at a time
        data.append(obj)  # Add each object to the data list
    return render(request, 'bennett.html', {'data': data})
def vdg(request):
    queryset = VendorData_Galgotia.objects.all()
    
    # Prepare a list to store data (or process it as needed)
    data = []
    for obj in queryset.iterator():  # Efficiently fetch one record at a time
        data.append(obj)  # Add each object to the data list
    return render(request, 'gal.html', {'data': data})
def vds(request):
    queryset = VendorData_sharda.objects.all()
    
    # Prepare a list to store data (or process it as needed)
    data = []
    for obj in queryset.iterator():  # Efficiently fetch one record at a time
        data.append(obj)  # Add each object to the data list
    return render(request, 'sharda.html', {'data': data})
def vdd(request):
    queryset = VendorData_Dtu.objects.all()
    
    # Prepare a list to store data (or process it as needed)
    data = []
    for obj in queryset.iterator():  # Efficiently fetch one record at a time
        data.append(obj)  # Add each object to the data list
    return render(request, 'Dtu.html', {'data': data})