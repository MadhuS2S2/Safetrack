# Generated by Django 5.0.1 on 2024-03-03 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kitchencenter', '0002_tasklist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasklist',
            new_name='tbl_tasklist',
        ),
    ]
