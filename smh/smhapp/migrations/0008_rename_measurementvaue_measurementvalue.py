# Generated by Django 3.2.5 on 2021-08-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smhapp', '0007_alter_device_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeasurementVaue',
            new_name='MeasurementValue',
        ),
    ]