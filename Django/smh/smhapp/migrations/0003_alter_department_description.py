# Generated by Django 3.2.5 on 2021-08-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smhapp', '0002_alter_department_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]