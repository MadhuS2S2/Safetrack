from django.db import models
from Guest.models import *

# Create your models here.

class tbl_sendcomplaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=30)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)

class tbl_userfeedback(models.Model):
    feedback_content=models.CharField(max_length=30)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
  