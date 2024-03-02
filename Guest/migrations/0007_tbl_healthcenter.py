# Generated by Django 5.0.1 on 2024-03-02 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_admin'),
        ('Guest', '0006_delete_tbl_healthcenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_healthcenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=30)),
                ('center_address', models.CharField(max_length=30)),
                ('center_proof', models.FileField(upload_to='images/')),
                ('center_photo', models.FileField(upload_to='images/')),
                ('center_email', models.CharField(max_length=30)),
                ('center_password', models.CharField(max_length=30)),
                ('center_ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_ward')),
            ],
        ),
    ]
