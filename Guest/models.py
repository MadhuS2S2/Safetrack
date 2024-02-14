from django.db import models

# Create your models here.

class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_photo=models.FileField(upload_to='images/')
    user_dob = models.CharField(max_length=30)
    user_gender = models.CharField(max_length=30)
    user_ward=models.CharField(max_length=30)
    user_address = models.CharField(max_length=30)
    user_proof = models.FileField(upload_to='images/')
    user_email = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)

class tbl_wardmember(models.Model):
    member_name = models.CharField(max_length=30)
    member_gender = models.CharField(max_length=30)
    member_ward=models.CharField(max_length=30)
    member_address = models.CharField(max_length=30)
    member_proof = models.CharField(max_length=30)
    member_photo = models.FileField(upload_to='images/')
    member_email = models.CharField(max_length=30)
    member_password = models.CharField(max_length=30)
    
class tbl_ashaworker(models.Model):
    worker_name = models.CharField(max_length=30)
    worker_gender = models.CharField(max_length=30)
    worker_ward=models.CharField(max_length=30)
    worker_address = models.CharField(max_length=30)
    worker_proof = models.CharField(max_length=30)
    worker_photo = models.FileField(upload_to='images/')
    worker_email = models.CharField(max_length=30)
    worker_password = models.CharField(max_length=30)

class tbl_healthcenter(models.Model):
    center_name = models.CharField(max_length=30)
    center_gender = models.CharField(max_length=30)
    center_ward = models.CharField(max_length=30)
    center_address = models.CharField(max_length=30)
    center_proof =  models.FileField(upload_to='images/')
    center_photo = models.FileField(upload_to='images/')
    center_email = models.CharField(max_length=30)
    center_password = models.CharField(max_length=30)
    
class tbl_viraldiseases(models.Model):
    disease_name=models.CharField(max_length=30)
    disease_mode=models.CharField(max_length=30)
    
