# Generated by Django 3.0.3 on 2020-02-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20200225_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='doctor_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='patient_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
