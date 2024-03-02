from django.db import models

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=10)
    admin_email=models.CharField(max_length=10)
    admin_password=models.CharField(max_length=10)

class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)
    
# Create your models here.
class tbl_panchayat(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)
    panchayat_name=models.CharField(max_length=30)
    panchayat_dateofjoin=models.CharField(max_length=30)
    panchayat_contact=models.CharField(max_length=30)
    panchayat_address=models.CharField(max_length=30)
    panchayat_email=models.CharField(max_length=30)
    panchayat_password=models.CharField(max_length=30)
    panchayat_photo=models.FileField(upload_to='images/')
    
class tbl_ward(models.Model):
    panchayat=models.ForeignKey(tbl_panchayat,on_delete=models.CASCADE,null=True)
    ward_name=models.CharField(max_length=30)
    
