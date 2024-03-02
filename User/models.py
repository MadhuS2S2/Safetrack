from django.db import models
from Guest.models import *
from HealthCenter.models import *
# Create your models here.
class tbl_sendcomplaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_content=models.CharField(max_length=100)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=100)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)

class tbl_userfeedback(models.Model):
    feedback_content=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
  
class tbl_medicinerequest(models.Model):
    medicine_prescription = models.CharField(max_length=30)
    medicine_date = models.DateField(auto_now_add=True)
    patient_id=models.ForeignKey(tbl_patient,on_delete=models.CASCADE,null=True)
    
class tbl_foodrequest(models.Model):
    food_date = models.DateField(auto_now_add=True)
    food_status = models.CharField(max_length=20)
    patient_id=models.ForeignKey(tbl_patient,on_delete=models.CASCADE,null=True)