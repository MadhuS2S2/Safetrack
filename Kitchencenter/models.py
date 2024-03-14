from django.db import models
from Guest.models import *

# Create your models here.
class tbl_foodlist(models.Model):
    food_name = models.CharField(max_length=30)
    food_date = models.DateField(auto_now_add=True)
    kitchen=models.ForeignKey(tbl_kitchencenter,on_delete=models.CASCADE,null=True)
    
class tbl_tasklist(models.Model):
    task_title=models.CharField( max_length=50)
    patient_name=models.CharField( max_length=50)
    patient_address=models.CharField( max_length=50)
    patient_ward=models.CharField( max_length=50)
    task_date=models.DateField(auto_now_add=True)
    task_status=models.CharField( max_length=50)