from django.db import models

# Create your models here.
class tbl_patient(models.Model):
    patient_name = models.CharField(max_length=20)
    patient_age = models.CharField(max_length=30)
    patient_gender = models.CharField(max_length=30)
    patient_admitdate = models.CharField(max_length=30)
    patient_dischargedate = models.CharField(max_length=30)
    patient_ward=models.CharField( max_length=50)
    patient_vstatus = models.CharField(max_length=30)
    
class tbl_medicinelist(models.Model):
    medicine_prescription = models.CharField(max_length=30)
    medicine_date = models.DateField(auto_now_add=True)
    

