# Generated by Django 5.0.1 on 2024-03-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCenter', '0012_delete_tbl_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20)),
                ('patient_age', models.CharField(max_length=30)),
                ('patient_gender', models.CharField(max_length=30)),
                ('patient_contact', models.IntegerField(max_length=30)),
                ('patient_admitdate', models.DateField(auto_now_add=True)),
                ('patient_dischargedate', models.CharField(max_length=30)),
                ('patient_ward', models.CharField(max_length=50)),
                ('patient_vstatus', models.CharField(max_length=30)),
            ],
        ),
    ]