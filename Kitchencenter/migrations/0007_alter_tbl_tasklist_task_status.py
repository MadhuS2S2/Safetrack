# Generated by Django 5.0.1 on 2024-03-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kitchencenter', '0006_tbl_tasklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_tasklist',
            name='task_status',
            field=models.CharField(max_length=50),
        ),
    ]
