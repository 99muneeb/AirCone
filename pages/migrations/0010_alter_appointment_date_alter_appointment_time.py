# Generated by Django 4.0.6 on 2022-08-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_rename_appointment_address_appointment_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=255),
        ),
    ]
