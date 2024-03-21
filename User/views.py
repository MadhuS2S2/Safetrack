from django.shortcuts import render,redirect
from Guest.models import *
from .models import *
from HealthCenter.models import *
from Kitchencenter.models import *
# Create your views here.
def userprofile(request):
        user = tbl_user.objects.get(id=request.session['uid'])
        return render(request,'User/UserProfile.html',{'user':user})

def editprofile(request):
        user = tbl_user.objects.get(id=request.session['uid'])
        if request.method == 'POST':
                if request.FILES.get('photo'):
                        user.user_photo=request.FILES.get('photo')
                        user.user_name = request.POST.get('name')
                        user.user_dob = request.POST.get('dob')
                        user.user_gender = request.POST.get('gender')
                        # user.centre_contact=request.POST.get('contact')
                        user.user_email = request.POST.get('email')
                        user.user_ward.ward_name=request.POST.get('ward')
                        user.save()
                        return redirect('User:userprofile')
                else:
                        user.user_name = request.POST.get('name')
                        user.user_dob = request.POST.get('dob')
                        user.user_gender = request.POST.get('gender')
                        # user.centre_contact=request.POST.get('contact')
                        user.user_email = request.POST.get('email')
                        user.user_ward.ward_name=request.POST.get('ward')
                        user.save()
                        return redirect('User:userprofile')
        else:
                return render(request,'User/UserEdit.html',{'user':user})

def change_password(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        currentpass=request.POST.get("currentpassword")
        if user.user_password == currentpass:
            newpass=request.POST.get("newpassword")
            conpass=request.POST.get("confirmpassword")
            if newpass==conpass:
                user.user_password=newpass
                user.save()
                msg="successfully"
                return render(request,'User/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'User/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'User/ChangePassword.html',{'msg':msg,'user':user})
    else:
        return render(request,'User/ChangePassword.html')
    
def home_page(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Homepage.html',{'user':user})

def sendcomplaint(request):
    complaint=tbl_sendcomplaint.objects.all()
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        tbl_sendcomplaint.objects.create(complaint_title=title,complaint_content=content,complaint_reply='not replied',user_id=user)
        return render(request,'User/SendComplaint.html')
    else:
        return render(request,'User/SendComplaint.html')
        
def userfeedback(request):
    feedback=tbl_userfeedback.objects.all()
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=='POST':
        feedback=request.POST.get('feedback')
        tbl_userfeedback.objects.create(feedback_content=feedback,user_id=user)
        return render(request,'User/Feedback.html')
    else:
        return render(request,'User/Feedback.html')

def viewcomplaint(request):
        complaint = tbl_sendcomplaint.objects.all()
        return render(request,'User/ViewComplaint.html',{'complaint':complaint})

def deletecomplaint(request,id):
    tbl_sendcomplaint.objects.get(id=id).delete()
    return redirect("User:usercomplaint")

def medicinelist(request):
        user=tbl_user.objects.get(id=request.session['uid'])
        wardid=user.user_ward
        medicinedata=tbl_medicinelist.objects.filter(Healthuser__user_ward=wardid)
        return render(request,'User/Medicinelist.html',{'medicine':medicinedata})

def foodlist(request):
        user=tbl_user.objects.get(id=request.session['uid'])
        wardid=user.user_ward
        fooddata=tbl_foodlist.objects.filter(kitchen__kitchen_ward=wardid)
        return render(request,'User/Foodlist.html',{'food':fooddata})
        
def requestmedicine(request,id):
        medicine=tbl_medicinelist.objects.get(id=id)
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_medicinerequest.objects.create(medicine_prescription=medicine.medicine_prescription,user_id=user)
        return redirect("User:medicinelist")
    
def requestfood(request,id):
        food=tbl_foodlist.objects.get(id=id)
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_foodrequest.objects.create(food_name=food.food_name,user_id=user)
        return redirect("User:foodlist")