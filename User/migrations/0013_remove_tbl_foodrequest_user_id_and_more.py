# Generated by Django 5.0.1 on 2024-03-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_tbl_medicinerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_foodrequest',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tbl_medicinerequest',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tbl_sendcomplaint',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tbl_userfeedback',
            name='user_id',
        ),
    ]