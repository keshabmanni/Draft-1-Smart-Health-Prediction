# Generated by Django 3.0.3 on 2020-02-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease_database', '0002_remove_diseasedatabasemodel_upload_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainedMlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trained_model', models.FileField(upload_to='trained model/')),
                ('accuracy', models.CharField(default='0', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='diseasedatabasemodel',
            name='File_Path',
            field=models.FileField(upload_to='dataset/'),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='symptom',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
