# Generated by Django 5.0.1 on 2024-03-02 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCenter', '0007_tbl_foodrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_medicinerequest',
            name='patient_id',
        ),
    ]
