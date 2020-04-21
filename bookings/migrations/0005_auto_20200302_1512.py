# Generated by Django 3.0.3 on 2020-03-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20200302_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Attended', 'Attended')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='patient_email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]