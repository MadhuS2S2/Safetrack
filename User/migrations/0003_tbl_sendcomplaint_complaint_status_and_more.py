# Generated by Django 5.0.1 on 2024-02-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_tbl_userfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_sendcomplaint',
            name='complaint_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tbl_sendcomplaint',
            name='complaint_content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_sendcomplaint',
            name='complaint_reply',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tbl_sendcomplaint',
            name='complaint_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tbl_userfeedback',
            name='feedback_content',
            field=models.CharField(max_length=100),
        ),
    ]
