from django.shortcuts import render,redirect
from Guest.models import *
from HealthCenter.models import *
from Admin.models import *
# Create your views here.

def kitchenprofile(request):
        kitchendata = tbl_kitchencenter.objects.get(id=request.session['kid'])
        return render(request,'Kitchencenter/KitchenProfile.html',{'kitchen':kitchendata})

def kitchenedit(request):
        kitchen = tbl_kitchencenter.objects.get(id=request.session['kid'])
        if request.method == 'POST':
                kitchen.kitchen_name = request.POST.get('name')
                kitchen.kitchen_address=request.POST.get('address')
                kitchen.kitchen_contact=request.POST.get('contact')
                kitchen.kitchen_email = request.POST.get('email')
                kitchen.kitchen_password = request.POST.get('password')
                kitchen.kitchen_district=request.POST.get('district')
                kitchen.save()
                return render(request,'Kitchencenter/KitchenEdit.html',{'kitchen':kitchen})
        else:
                return render(request,'Kitchencenter/KitchenEdit.html',{'kitchen':kitchen})

def home_page(request):
    kitchendata=tbl_kitchencenter.objects.get(id=request.session['kid'])
    return render(request,'Kitchencenter/Homepage.html',{'kitchen':kitchendata})

def viewrequest(request):
    requestdata = tbl_foodrequest.objects.all()
    return render(request,'Kitchencenter/ViewRequests.html',{'requestdata':requestdata})

# def foodstatus(request,sid):
#     requestdata = tbl_foodrequest.objects.get(id=sid)
    

# def change_password(request):
#     centre=tbl_healthcenter.objects.get(id=request.session['cid'])
#     if request.method=="POST":
#         currentpass=request.POST.get("currentpassword")
#         if centre.center_password == currentpass:
#             newpass=request.POST.get("newpassword")
#             conpass=request.POST.get("confirmpassword")
#             if newpass==conpass:
#                 centre.centre_password=newpass
#                 centre.save()
#                 msg="successfully"
#                 return render(request,'Healthcenter/ChangePassword.html',{'msg':msg})
#             else:
#                 msg="Cannot Change Password"
#                 return render(request,'Healthcenter/ChangePassword.html',{'msg':msg})
#         else:
#             msg="Password Incorrect"
#             return render(request,'Healthcenter/ChangePassword.html',{'msg':msg,'centre':centre})
#     else:
#         return render(request,'Healthcenter/ChangePassword.html')
    