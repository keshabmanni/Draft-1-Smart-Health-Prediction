# Generated by Django 3.0.3 on 2020-03-25 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200305_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeddoctorsdetail',
            name='total_book_per_day',
        ),
    ]
