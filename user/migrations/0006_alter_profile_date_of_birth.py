# Generated by Django 4.2.11 on 2024-04-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profile_date_of_birth_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
