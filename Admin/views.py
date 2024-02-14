from django.shortcuts import render,redirect
from .models import *
from Guest.models import *
from User.models import *
# Create your views here.
def district(request):
    district_data=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('district')
        tbl_district.objects.create(district_name=district)
        return redirect("Admin:district")
    else:
        return render(request,'Admin/District.html',{'district':district_data})

def panchayat(request):
    panchayat_data=tbl_panchayat.objects.all()
    district_data=tbl_district.objects.all()
    
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('dropdown'))
        panchayat=request.POST.get("panchayat")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        date=request.POST.get("dateofjoin")
        photo=request.FILES.get("photo")
        email=request.POST.get("email")
        password=request.POST.get('password')
        
        tbl_panchayat.objects.create(panchayat_name=panchayat,panchayat_dateofjoin=date,panchayat_contact=contact,panchayat_address=address,panchayat_email=email,panchayat_password=password,panchayat_photo=photo,district=district)
        return render(request,"Admin/panchayat.html",{"district":district_data,"panchayat":panchayat_data})
    else:
        return render(request,"Admin/panchayat.html",{"district":district_data,"panchayat":panchayat_data})

def ward(request):
    district_data=tbl_district.objects.all()
    panchayat_data=tbl_panchayat.objects.all()
    ward_data=tbl_ward.objects.all()
        
    if request.method=='POST':
        ward=request.POST.get('ward')
        district=tbl_district.objects.get(id=request.POST.get('disdrop'))
        panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
        tbl_ward.objects.create(ward_name=ward,panchayat=panchayat)
        
        return render(request,"Admin/ward.html",{'district':district_data,'panchayat':panchayat_data,'ward':ward_data})
    else:
        return render(request,"Admin/ward.html",{'district':district_data,'panchayat':panchayat_data,'ward':ward_data})

def ajaxward(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))
    panchayat = tbl_panchayat.objects.filter(district_id=district)
    return render(request,"Admin/Ajax.html",{"panchayat":panchayat })

def viewcomplaint(request):
        complaint = tbl_sendcomplaint.objects.all()
        return render(request,'Admin/ViewComplaint.html',{'complaint':complaint})

def deletecomplaint(request,id):
    tbl_sendcomplaint.objects.get(id=id).delete()
    return redirect("Admin:usercomplaint")

def reply(request,id):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        reply = request.POST.get("reply")
        tbl_sendcomplaint.objects.create(complaint_reply=reply,user_id=user)
        return render(request,"Admin/Reply.html")
    else:
        return render(request,"Admin/Reply.html")