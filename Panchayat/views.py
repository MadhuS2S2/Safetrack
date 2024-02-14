from django.shortcuts import render
from Guest.models import *
from Admin.models import *
# Create your views here.

def viewprofile(request):
        panchayat = tbl_panchayat.objects.get(id=request.session['pid'])
        return render(request,'Panchayat/PanchayatProfile.html',{'panchayat':panchayat})

def editprofile(request):
        panchayat = tbl_panchayat.objects.get(id=request.session['pid'])
        if request.method == 'POST':
                panchayat.panchayat_name = request.POST.get('name')
                panchayat.panchayat_dateofjoin=request.POST.get('date')
                panchayat.panchayat_contact=request.POST.get('contact')
                panchayat.panchayat_email = request.POST.get('email')
                panchayat.panchayat_password = request.POST.get('password')
                panchayat.panchayat_district=request.POST.get('district')
                panchayat.save()
                return render(request,'Panchayat/PanchayatEdit.html',{'panchayat':panchayat})
        else:
                return render(request,'Panchayat/panchayatEdit.html',{'panchayat':panchayat})

def change_password(request):
    panchayat=tbl_panchayat.objects.get(id=request.session['pid'])
    if request.method=="POST":
        currentpass=request.POST.get("currentpassword")
        if panchayat.panchayat_password == currentpass:
            newpass=request.POST.get("newpassword")
            conpass=request.POST.get("confirmpassword")
            if newpass==conpass:
                panchayat.panchayat_password=newpass
                panchayat.save()
                msg="successfully"
                return render(request,'Panchayat/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'Panchayat/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Panchayat/ChangePassword.html',{'msg':msg,'panchayat':panchayat})
    else:
        return render(request,'Panchayat/ChangePassword.html')
    
def home_page(request):
    panchayat=tbl_panchayat.objects.get(id=request.session['pid'])
    return render(request,'Panchayat/Homepage.html',{'panchayat':panchayat})