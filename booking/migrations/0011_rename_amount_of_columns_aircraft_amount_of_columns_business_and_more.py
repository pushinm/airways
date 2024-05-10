# Generated by Django 4.2.11 on 2024-04-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_flightschedule_flightdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraft',
            old_name='amount_of_columns',
            new_name='amount_of_columns_business',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='amount_of_columns_econom',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='amount_of_columns_premium',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
