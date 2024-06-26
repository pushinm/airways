# Generated by Django 4.2.11 on 2024-04-26 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_delete_newaircraft'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.RemoveField(
            model_name='aircraft',
            name='seat_class',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='amount_of_columns',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='business_class_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='econom_class_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='premium_class_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='airfare',
            name='aircraft',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='aircraft', to='booking.aircraft'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flightschedule',
            name='airCraft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_sch', to='booking.aircraft'),
        ),
        migrations.DeleteModel(
            name='SeatCategory',
        ),
    ]
