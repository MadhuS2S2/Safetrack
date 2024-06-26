# Generated by Django 5.0.1 on 2024-02-12 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_panchayat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panchayat_name', models.CharField(max_length=30)),
                ('panchayat_dateofjoin', models.CharField(max_length=30)),
                ('panchayat_contact', models.CharField(max_length=30)),
                ('panchayat_address', models.CharField(max_length=30)),
                ('panchayat_email', models.CharField(max_length=30)),
                ('panchayat_password', models.CharField(max_length=30)),
                ('panchayat_photo', models.FileField(upload_to='images/')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(max_length=30)),
                ('panchayat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_panchayat')),
            ],
        ),
    ]
