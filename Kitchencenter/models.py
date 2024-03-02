from django.db import models

# Create your models here.
class tbl_foodlist(models.Model):
    food_name = models.CharField(max_length=30)
    food_date = models.DateField(auto_now_add=True)