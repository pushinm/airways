# Generated by Django 4.2.11 on 2024-04-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_flightschedule_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightschedule',
            name='flightDate',
            field=models.DateField(),
        ),
    ]