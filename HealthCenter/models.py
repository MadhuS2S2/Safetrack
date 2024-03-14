from django.db import models
from Guest.models import *
# Create your models here.
class tbl_patient(models.Model):
    patient_name = models.CharField(max_length=20)
    patient_age = models.CharField(max_length=30)
    patient_gender = models.CharField(max_length=30)
    patient_contact = models.IntegerField()
    patient_admitdate = models.DateField(auto_now_add=True)
    patient_dischargedate = models.CharField(max_length=30)
    patient_ward=models.CharField( max_length=50)
    patient_vstatus = models.CharField(max_length=30)
    
class tbl_medicinelist(models.Model):
    medicine_prescription = models.CharField(max_length=30)
    medicine_date = models.DateField(auto_now_add=True)
    Healthcenter=models.ForeignKey(tbl_healthcenter,on_delete=models.CASCADE,null=True)
    

