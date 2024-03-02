from django.shortcuts import render
from Guest.models import *
# Create your views here.

def workerprofile(request):
        worker = tbl_ashaworker.objects.get(id=request.session['wid'])
        return render(request, 'AshaWorker/workerprofile.html',{'worker': worker})
        
def workeredit(request):
        worker = tbl_ashaworker.objects.get(id=request.session['wid'])
        if request.method == 'POST':
                worker.worker_name = request.POST.get('name')
                worker.worker_dateofjoin=request.POST.get('gender')
                worker.worker_contact=request.POST.get('contact')
                worker.worker_email = request.POST.get('email')
                worker.worker_password = request.POST.get('password')
                worker.worker_district=request.POST.get('district')
                worker.save()
                return render(request,'AshaWorker/WorkerEdit.html',{'worker':worker})
        else:
                return render(request,'AshaWorker/WorkerEdit.html',{'worker':worker})
        
def change_password(request):
    worker=tbl_ashaworker.objects.get(id=request.session['wid'])
    if request.method=="POST":
        currentpass=request.POST.get("currentpassword")
        if worker.worker_password == currentpass:
            newpass=request.POST.get("newpassword")
            conpass=request.POST.get("confirmpassword")
            if newpass==conpass:
                worker.worker_password=newpass
                worker.save()
                msg="successfully"
                return render(request,'AshaWorker/ChangePassword.html',{'msg':msg})
            else:
                msg="Cannot Change Password"
                return render(request,'AshaWorker/ChangePassword.html',{'msg':msg})
        else:
            msg="Password Incorrect"
            return render(request,'AshaWorker/ChangePassword.html',{'msg':msg,'worker':worker})
    else:
        return render(request,'AshaWorker/ChangePassword.html')
    
def home_page(request):
    worker=tbl_ashaworker.objects.get(id=request.session['wid'])
    return render(request,'AshaWorker/Homepage.html',{'worker':worker})