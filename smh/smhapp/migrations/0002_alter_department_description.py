# Generated by Django 3.2.5 on 2021-08-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smhapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]