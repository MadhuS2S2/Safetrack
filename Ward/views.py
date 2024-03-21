from django.shortcuts import render,redirect
from Guest.models import *
from HealthCenter.models import *
from .models import *

# Create your views here.
def memberprofile(request):
        member = tbl_wardmember.objects.get(id=request.session['mid'])
        return render(request,'Ward/Wardprofile.html',{'ward':member})
    
def home_page(request):
        member=tbl_wardmember.objects.get(id=request.session['mid'])
        return render(request,'Ward/Homepage.html',{'ward':member})

def memberedit(request):
        member = tbl_wardmember.objects.get(id=request.session['mid'])
        if request.method == 'POST':
                ward=tbl_ward.objects.get(id=request.POST.get('ward')) 
                if request.FILES.get('photo'):
                        member.member_photo=request.FILES.get('photo')
                        member.member_name = request.POST.get('name')
                        member.member_gender = request.POST.get('gender')
                        member.member_address = request.POST.get('address')
                        member.member_ward = ward
                        member.member_email = request.POST.get('email')
                        # member.member_proof= request.POST.get('proof')
                        member.save()
                        return redirect('Ward:memberprofile')
                else:
                        member.member_name = request.POST.get('name')
                        member.member_gender = request.POST.get('gender')
                        member.member_address = request.POST.get('address')
                        member.member_ward = ward
                        member.member_email = request.POST.get('email')
                        # member.member_proof= request.POST.get('proof')
                        member.save()
                        return redirect('Ward:memberprofile')
        else:
                return render(request,'Ward/MemberEdit.html',{'member':member})

def change_password(request):
    member=tbl_wardmember.objects.get(id=request.session['mid'])
    if request.method=="POST":
        currentpass=request.POST.get("currentpassword")
        if member.member_password == currentpass:
            newpass=request.POST.get("newpassword")
            conpass=request.POST.get("confirmpassword")
            if newpass==conpass:
                member.member_password=newpass
                member.save()
                msg="successfully"
                return render(request,'Ward/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'Ward/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'Ward/ChangePassword.html',{'msg':msg,'member':member})
    else:
        return render(request,'Ward/ChangePassword.html')

def addpatient(request):
        patientdata=tbl_patient.objects.all()
        if request.method == 'POST':
                name=request.POST.get('name')
                age=request.POST.get('age')
                gender=request.POST.get('gender')
                date=request.POST.get('date')
                tbl_patient.objects.create(patient_name=name,patient_age=age,patient_gender=gender,patient_admitdate=date,patient_dischargedate=0,patient_vstatus=0)
                return render(request,'Healthcenter/ViewPatients.html',{'patient':patientdata})
        else:
                return render(request,'Healthcenter/AddPatient.html',{'patient':patientdata})
        
def viewpatient(request):
        patientdata = tbl_patient.objects.all()
        return render(request,'Healthcenter/ViewPatients.html',{'patient':patientdata})

def medicinerequest(request):
        medicinedata=tbl_medicinerequest.objects.all()
        if request.method=='POST':
                prescription=request.POST.get('prescription')
                tbl_medicinerequest.objects.create(medicine_prescription=prescription)
                return render(request,'Healthcenter/MedicineRequest.html',{'medicine':medicinedata})
        else:
                return render(request,'Healthcenter/MedicineRequest.html',{'medicine':medicinedata})

def deletepatient(request,id):
    tbl_patient.objects.get(id=id).delete()
    return redirect("Healthcenter:addpatient")

def deletekitchen(request,id):
    tbl_kitchen.objects.get(id=id).delete()
    return redirect("Ward:addkitchen")

def kitchenreg(request):
        kitchendata=tbl_kitchen.objects.all()
        if request.method == 'POST':
                name=request.POST.get('name')
                contact=request.POST.get('contact')
                address=request.POST.get('address')
                email=request.POST.get('email')
                password=request.POST.get('password')
                tbl_kitchen.objects.create(kitchen_name=name,kitchen_contact=contact,kitchen_address=address,kitchen_email=email,kitchen_password=password)
                return render(request,'Ward/KitchenRegistration.html',{'kitchen':kitchendata})
        else:
                return render(request,'Ward/KitchenRegistration.html',{'kitchen':kitchendata})
            
def viewkitchen(request):
        kitchendata = tbl_kitchen.objects.all()
        return render(request,'Ward/ViewKitchens.html',{'kitchen':kitchendata})

def PatientReport(request):
        member=tbl_wardmember.objects.get(id=request.session['mid'])
        warddata=member.member_ward
        print(warddata)
        if request.method == 'POST':
                fromdate=request.POST.get('from_date')
                # todate=request.POST.get('to_date')
                patient=tbl_patient.objects.filter(patient_admitdate__gte=fromdate,patient_admitdate__lte=todate,patient_ward=warddata.id,patient_vstatus=0)
                print(patient)
                return render(request,'Ward/Report.html',{'data':patient})
        else:
                return render(request,'Ward/Report.html')
        
def PatientcountReport(request):
        member=tbl_wardmember.objects.get(id=request.session['mid'])
        warddata=member.member_ward
        # print(warddata)
        patient=tbl_patient.objects.filter(patient_ward=warddata.id,patient_vstatus=0).count()
        discharged=tbl_patient.objects.filter(patient_ward=warddata.id,patient_vstatus=1).count()
        print(patient)
        return render(request,'Ward/PatientCountReport.html',{'data':patient,'discharged':discharged})
        