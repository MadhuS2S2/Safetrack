# Generated by Django 5.0.1 on 2024-02-17 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCenter', '0003_tbl_medicinerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_patient',
            name='patient_admitdate',
        ),
        migrations.RemoveField(
            model_name='tbl_patient',
            name='patient_age',
        ),
        migrations.RemoveField(
            model_name='tbl_patient',
            name='patient_dischargedate',
        ),
        migrations.RemoveField(
            model_name='tbl_patient',
            name='patient_gender',
        ),
        migrations.RemoveField(
            model_name='tbl_patient',
            name='patient_vstatus',
        ),
    ]
