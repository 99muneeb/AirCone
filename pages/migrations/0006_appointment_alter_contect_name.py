# Generated by Django 4.0.6 on 2022-08-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_team_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.TextField()),
                ('data', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('datatime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contect',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
