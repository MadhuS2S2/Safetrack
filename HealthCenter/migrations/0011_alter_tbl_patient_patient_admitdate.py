# Generated by Django 5.0.1 on 2024-03-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCenter', '0010_tbl_medicinelist_healthcenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_patient',
            name='patient_admitdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]