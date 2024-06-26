# Generated by Django 5.0.1 on 2024-02-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_medicinerequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_prescription', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_age', models.CharField(max_length=30)),
                ('patient_gender', models.CharField(max_length=30)),
                ('patient_admitdate', models.CharField(max_length=30)),
                ('patient_dischargedate', models.CharField(max_length=30)),
                ('patient_vstatus', models.CharField(max_length=30)),
            ],
        ),
    ]
