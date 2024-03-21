from django.shortcuts import render,redirect
from Guest.models import *
from .models import *
from Admin.models import *
from User.models import *
from Kitchencenter.models import *
from datetime import datetime
# Create your views here.

def centreprofile(request):
        Healthcenter = tbl_healthcenter.objects.get(id=request.session['cid'])
        return render(request,'Healthcenter/CenterProfile.html',{'profile':Healthcenter})

def centreedit(request):
        centre = tbl_healthcenter.objects.get(id=request.session['cid'])
        if request.method == 'POST':
                if request.FILES.get('photo'):
                        centre.center_photo=request.FILES.get('photo')
                        centre.center_name = request.POST.get('name')
                        # centre.centre_contact=request.POST.get('contact')
                        centre.center_email = request.POST.get('email')
                        centre.center_ward.ward_name=request.POST.get('ward')
                        centre.save()
                        return redirect('Healthcenter:centreprofile')
                else:
                        centre.center_name = request.POST.get('name')
                        # centre.centre_contact=request.POST.get('contact')
                        centre.center_email = request.POST.get('email')
                        centre.center_ward.ward_name=request.POST.get('ward')
                        centre.save()
                        return redirect('Healthcenter:centreprofile')
        else:
                return render(request,'Healthcenter/CenterEdit.html',{'center':centre})

def change_password(request):
    centre=tbl_healthcenter.objects.get(id=request.session['cid'])
    if request.method=="POST":
        currentpass=request.POST.get("currentpassword")
        if centre.center_password == currentpass:
            newpass=request.POST.get("newpassword")
            
            conpass=request.POST.get("confrimpassword")
            print(request.POST.get("currentpassword"))
            if newpass==conpass:
                centre.center_password=newpass
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
        warddata=centre.center_ward
        patient=tbl_patient.objects.all().count()
        admitted=tbl_patient.objects.filter(patient_ward=warddata.id,patient_vstatus=0).count()
        discharged=tbl_patient.objects.filter(patient_ward=warddata.id,patient_vstatus=1).count()
        print(discharged)
        return render(request,'Healthcenter/Homepage.html',{'centre':centre,'patient':patient,'discharged':discharged,'admitted':admitted})


def addpatient(request):
        patientdata=tbl_patient.objects.all()
        district_data=tbl_district.objects.all()
        panchayat_data=tbl_panchayat.objects.all()
        ward_data=tbl_ward.objects.all()
        
        if request.method == 'POST':
                name=request.POST.get('name')
                age=request.POST.get('age')
                gender=request.POST.get('gender')
                contact=request.POST.get('phone')
                date=request.POST.get('date')
                
                district=tbl_district.objects.get(id=request.POST.get('disdrop'))
                panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
                ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
                tbl_patient.objects.create(patient_name=name,patient_age=age,patient_gender=gender,patient_contact=contact,patient_dischargedate=0,patient_ward=ward.id,patient_vstatus=0)
                return render(request,'Healthcenter/ViewPatients.html',{'patient':patientdata,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
        else:
                return render(request,'Healthcenter/AddPatient.html',{'patient':patientdata,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
        
def viewpatient(request):
        patientdata = tbl_patient.objects.all()
        return render(request,'Healthcenter/ViewPatients.html',{'patient':patientdata})

def addmedicines(request):
        medicinedata=tbl_medicinerequest.objects.all()
        centre=tbl_healthcenter.objects.get(id=request.session['cid'])
        
        if request.method=='POST':
                prescription=request.POST.get('prescription')
                tbl_medicinelist.objects.create(medicine_prescription=prescription,Healthcenter=centre)
                return render(request,'Healthcenter/Addmedicines.html')
        else:
                return render(request,'Healthcenter/Addmedicines.html',{'medicine':medicinedata})

def deletepatient(request,id):
    tbl_patient.objects.get(id=id).delete()
    return redirect("Healthcenter:addpatient")

def patientdischarge(request,id):
        current_date = datetime.now()
        patient=tbl_patient.objects.get(id=id)
        patient.patient_vstatus=1
        patient.patient_dischargedate=current_date
        patient.save()
        return redirect("Healthcenter:viewpatient")
        

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

# def foodrequest(request,fid):
#         patient=tbl_patient.objects.get(id=fid)
#         fooddata = tbl_foodrequest.objects.all()
#         tbl_foodrequest.objects.create(patient_id=patient)
#         return redirect("Healthcenter:viewpatient")
     
def requestlist(request):
        medicinedata=tbl_medicinerequest.objects.all()
        return render(request,'Healthcenter/Viewrequests.html',{'medicine':medicinedata})

def assigntask(request,id):
        medicine=tbl_medicinerequest.objects.get(id=id)
        tbl_tasklist.objects.create(task_title="Deliver Medicine",patient_name=medicine.user_id.user_name,patient_address=medicine.user_id.user_address,patient_ward=medicine.user_id.user_ward.ward_name,task_status=1)
        return redirect("Healthcenter:requestlist")

def PatientReport(request):
        center=tbl_healthcenter.objects.get(id=request.session['cid'])
        warddata=center.center_ward
        if request.method == 'POST':
                fromdate=request.POST.get('from_date')
                todate=request.POST.get('to_date')
                patient=tbl_patient.objects.filter(patient_admitdate__gte=fromdate,patient_admitdate__lte=todate,patient_ward=warddata.id,patient_vstatus=0)
                return render(request,'Healthcenter/Report.html',{'data':patient})
        else:
                return render(request,'Healthcenter/Report.html')
        
def PatientcountReport(request):
        center=tbl_healthcenter.objects.get(id=request.session['cid'])
        warddata=center.center_ward
        patient=tbl_patient.objects.filter(patient_ward=warddata.id,patient_vstatus=0).count()
        discharged=tbl_patient.objects.filter(patient_ward=warddata.id,patient_vstatus=1).count()
        print(discharged)
        return render(request,'Healthcenter/PatientCountReport.html',{'patient':patient,'discharged':discharged})