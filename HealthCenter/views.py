from django.shortcuts import render,redirect
from Guest.models import *
from .models import *
from Admin.models import *
# Create your views here.

def centreprofile(request):
        Healthcenter = tbl_healthcenter.objects.get(id=request.session['cid'])
        return render(request,'Healthcenter/CenterProfile.html',{'center':Healthcenter})

def centreedit(request):
        centre = tbl_healthcenter.objects.get(id=request.session['cid'])
        if request.method == 'POST':
                centre.centre_name = request.POST.get('name')
                centre.centre_contact=request.POST.get('contact')
                centre.centre_email = request.POST.get('email')
                centre.centre_password = request.POST.get('password')
                centre.centre_district=request.POST.get('district')
                centre.save()
                return render(request,'Healthcenter/CenterEdit.html',{'centre':centre})
        else:
                return render(request,'Healthcenter/CenterEdit.html',{'centre':centre})

def change_password(request):
    centre=tbl_healthcenter.objects.get(id=request.session['cid'])
    if request.method=="POST":
        currentpass=request.POST.get("currentpassword")
        if centre.center_password == currentpass:
            newpass=request.POST.get("newpassword")
            conpass=request.POST.get("confirmpassword")
            if newpass==conpass:
                centre.centre_password=newpass
                centre.save()
                msg="successfully"
                return render(request,'Healthcenter/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'Healthcenter/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Healthcenter/ChangePassword.html',{'msg':msg,'centre':centre})
    else:
        return render(request,'Healthcenter/ChangePassword.html')
    
def home_page(request):
    centre=tbl_healthcenter.objects.get(id=request.session['cid'])
    return render(request,'Healthcenter/Homepage.html',{'centre':centre})

def addpatient(request):
        patientdata=tbl_patient.objects.all()
        district_data=tbl_district.objects.all()
        panchayat_data=tbl_panchayat.objects.all()
        ward_data=tbl_ward.objects.all()
        
        if request.method == 'POST':
                name=request.POST.get('name')
                age=request.POST.get('age')
                gender=request.POST.get('gender')
                date=request.POST.get('date')
                
                district=tbl_district.objects.get(id=request.POST.get('disdrop'))
                panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
                ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
                tbl_patient.objects.create(patient_name=name,patient_age=age,patient_gender=gender,patient_admitdate=date,patient_dischargedate=0,patient_ward=ward,patient_vstatus=0)
                return render(request,'Healthcenter/ViewPatients.html',{'patient':patientdata,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
        else:
                return render(request,'Healthcenter/AddPatient.html',{'patient':patientdata,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
        
def viewpatient(request):
        patientdata = tbl_patient.objects.all()
        return render(request,'Healthcenter/ViewPatients.html',{'patient':patientdata})

def medicinerequest(request,id):
        patient=tbl_patient.objects.get(id=id)
        medicinedata=tbl_medicinerequest.objects.all()
        if request.method=='POST':
                prescription=request.POST.get('prescription')
                tbl_medicinerequest.objects.create(medicine_prescription=prescription,patient_id=patient)
                return render(request,'Healthcenter/MedicineRequest.html')
        else:
                return render(request,'Healthcenter/MedicineRequest.html',{'medicine':medicinedata})

def deletepatient(request,id):
    tbl_patient.objects.get(id=id).delete()
    return redirect("Healthcenter:addpatient")

def district(request):
    district_data=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('district')
        tbl_district.objects.create(district_name=district)
        return redirect("Healthcenter:district")
    else:
        return render(request,'Healthcenter/District.html',{'district':district_data})

def ajaxpan(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))
    panchayat = tbl_panchayat.objects.filter(district_id=district)
    return render(request,"Healthcenter/PanAjax.html",{"panchayat":panchayat})

def ajaxward(request):
    panchayat = tbl_panchayat.objects.get(id=request.GET.get("did"))
    ward = tbl_ward.objects.filter(panchayat_id=panchayat)
    return render(request,"Healthcenter/WardAjax.html",{"ward":ward })

def foodrequest(request,fid):
        patient=tbl_patient.objects.get(id=fid)
        fooddata = tbl_foodrequest.objects.all()
        tbl_foodrequest.objects.create(patient_id=patient)
        return redirect("Healthcenter:viewpatient")
     

