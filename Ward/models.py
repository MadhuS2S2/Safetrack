from django.db import models

# Create your models here.

class tbl_kitchen(models.Model):
    kitchen_name = models.CharField(max_length=30)
    kitchen_contact=models.CharField(max_length=30)
    kitchen_address = models.CharField(max_length=30)
    kitchen_email = models.EmailField(max_length=30)
    kitchen_password = models.CharField(max_length=30)