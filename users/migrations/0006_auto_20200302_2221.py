# Generated by Django 3.0.3 on 2020-03-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200302_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeddoctorsdetail',
            name='close_time',
        ),
        migrations.RemoveField(
            model_name='extendeddoctorsdetail',
            name='open_time',
        ),
        migrations.AlterField(
            model_name='extendeddoctorsdetail',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]