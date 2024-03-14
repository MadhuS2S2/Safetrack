from django.shortcuts import render,redirect
from .models import *
from Admin.models import *

def user(request):
    
    user_data=tbl_user.objects.all()
    district_data=tbl_district.objects.all()
    panchayat_data=tbl_panchayat.objects.all()
    ward_data=tbl_ward.objects.all()
    
    if request.method=='POST':
        name=request.POST.get('name')
        photo=request.FILES.get('photo')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        address=request.POST.get('address')

        ward=request.POST.get('warddrop')
        email=request.POST.get('email')
        password=request.POST.get('password')
        proof=request.FILES.get('proof')

        district=tbl_district.objects.get(id=request.POST.get('disdrop'))
        panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
        ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
        tbl_user.objects.create(user_name=name,user_photo=photo,user_dob=dob,user_gender=gender,user_ward=ward,user_address=address,user_proof=proof,user_email=email,user_password=password)
        
        return redirect("Guest:login")          
    else:
        return render(request,'Guest/User.html',{'user': user_data,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})

# Create your views here.
def ajaxpan(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))
    panchayat = tbl_panchayat.objects.filter(district_id=district)
    return render(request,"Guest/PanAjax.html",{"panchayat":panchayat })

def ajaxward(request):
    panchayat = tbl_panchayat.objects.get(id=request.GET.get("did"))
    ward = tbl_ward.objects.filter(panchayat_id=panchayat)
    return render(request,"Guest/WardAjax.html",{"ward":ward })

def wardmember(request):
    
    wardmember_data=tbl_wardmember.objects.all()
    district_data=tbl_district.objects.all()
    panchayat_data=tbl_panchayat.objects.all()
    ward_data=tbl_ward.objects.all()
    
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        address=request.POST.get('address')

        ward=request.POST.get('warddrop')
        email=request.POST.get('email')
        password=request.POST.get('password')
        photo=request.POST.get('photo')
        proof=request.POST.get('proof')
        
        district=tbl_district.objects.get(id=request.POST.get('disdrop'))
        panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
        ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
        tbl_wardmember.objects.create(member_name=name,member_gender=gender,member_ward=ward,member_address=address,member_proof=proof,member_photo=photo,member_email=email,member_password=password)
        
        return redirect("Guest/WardMember.html")        
    else:
        return render(request,'Guest/WardMember.html',{'wardmember': wardmember_data,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
    

def ashaworker(request):
    
    worker_data=tbl_ashaworker.objects.all()
    district_data=tbl_district.objects.all()
    panchayat_data=tbl_panchayat.objects.all()
    ward_data=tbl_ward.objects.all()
    
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        address=request.POST.get('address')

        ward=request.POST.get('warddrop')
        email=request.POST.get('email')
        password=request.POST.get('password')
        photo=request.POST.get('photo')
        proof=request.POST.get('proof')
        
        district=tbl_district.objects.get(id=request.POST.get('disdrop'))
        panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
        ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
        tbl_ashaworker.objects.create(worker_name=name,worker_gender=gender,worker_ward=ward,worker_address=address,worker_proof=proof,worker_photo=photo,worker_email=email,worker_password=password)
        
        return redirect("Guest:login")        
    else:
        return render(request,'Guest/AshaWorker.html',{'worker': worker_data,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
    
    
def healthcenter(request):
    
    center_data=tbl_healthcenter.objects.all()
    district_data=tbl_district.objects.all()
    panchayat_data=tbl_panchayat.objects.all()
    ward_data=tbl_ward.objects.all()
    
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')

        ward=request.POST.get('warddrop')
        email=request.POST.get('email')
        password=request.POST.get('password')
        photo=request.FILES.get('photo')
        proof=request.FILES.get('proof')
        
        district=tbl_district.objects.get(id=request.POST.get('disdrop'))
        panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
        ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
        tbl_healthcenter.objects.create(center_name=name,center_ward=ward,center_address=address,center_proof=proof,center_photo=photo,center_email=email,center_password=password)
        
        return redirect("Guest:login")        
    else:
        return render(request,'Guest/HealthCenter.html',{'center': center_data,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
    
def kitchencenter(request):
    
    kitchen_data=tbl_kitchencenter.objects.all()
    district_data=tbl_district.objects.all()
    panchayat_data=tbl_panchayat.objects.all()
    ward_data=tbl_ward.objects.all()
    
    if request.method=='POST':
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        address=request.POST.get('address')

        ward=request.POST.get('warddrop')
        email=request.POST.get('email')
        password=request.POST.get('password')
        photo=request.FILES.get('photo')
        proof=request.FILES.get('proof')
        
        district=tbl_district.objects.get(id=request.POST.get('disdrop'))
        panchayat=tbl_panchayat.objects.get(id=request.POST.get('pandrop'))
        ward=tbl_ward.objects.get(id=request.POST.get('warddrop')) 
        
        tbl_kitchencenter.objects.create(kitchen_name=name,kitchen_ward=ward,kitchen_address=address,kitchen_photo=photo,kitchen_email=email,kitchen_password=password)
        
        return redirect("Guest:login")        
    else:
        return render(request,'Guest/Kitchencenter.html',{'kitchen': kitchen_data,'district': district_data,'panchayat': panchayat_data,'ward':ward_data})
    
    
def login(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        panchayathcount = tbl_panchayat.objects.filter(panchayat_email=email,panchayat_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        workercount=tbl_ashaworker.objects.filter(worker_email=email,worker_password=password).count()
        centrecount=tbl_healthcenter.objects.filter(center_email=email,center_password=password).count()
        membercount=tbl_wardmember.objects.filter(member_email=email,member_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        kitchencount=tbl_kitchencenter.objects.filter(kitchen_email=email,kitchen_password=password).count()
        
        if admincount > 0 :
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:homepage')
        elif panchayathcount > 0:
            panchayat = tbl_panchayat.objects.get(panchayat_email=email,panchayat_password=password)
            request.session["pid"] = panchayat.id
            return redirect("panchayat:homepage")
        elif workercount > 0:
            worker = tbl_ashaworker.objects.get(worker_email=email,worker_password=password)
            request.session["wid"] = worker.id
            return redirect("Ashaworker:homepage")
        elif centrecount > 0:
            centre = tbl_healthcenter.objects.get(center_email=email,center_password=password)
            request.session["cid"] = centre.id
            return redirect("Healthcenter:homepage")
        elif membercount > 0:
            member = tbl_wardmember.objects.get(member_email=email,member_password=password)
            request.session["mid"] = member.id
            return redirect("Ward:homepage")
        elif usercount > 0:     
            user = tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"] = user.id
            return redirect("User:homepage")
        elif kitchencount > 0:     
            kitchen = tbl_kitchencenter.objects.get(kitchen_email=email,kitchen_password=password)
            request.session["kid"] = kitchen.id
            return redirect("kitchencenter:homepage")
        else:
            return render(request,'Guest/Login.html')
    else:
        return render(request,'Guest/Login.html')
    
def home_page(request):
    # worker=tbl_ashaworker.objects.get(id=request.session['wid'])
    return render(request,'Guest/Homepage.html')