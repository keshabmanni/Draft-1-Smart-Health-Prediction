# Generated by Django 3.0.3 on 2020-03-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20200225_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='address',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
