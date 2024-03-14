# Generated by Django 5.0.1 on 2024-03-03 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_tbl_healthcenter'),
        ('User', '0011_delete_tbl_medicinerequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_medicinerequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_prescription', models.CharField(max_length=30)),
                ('medicine_date', models.DateField(auto_now_add=True)),
                ('medicine_status', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
