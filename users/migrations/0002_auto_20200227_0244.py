# Generated by Django 3.0.3 on 2020-02-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedpatientsdetail',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('AndhraPradesh', 'Andhra Pradesh'), ('ArunachalPradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Sikkim', 'Sikkim'), ('Nagaland', 'Nagaland'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Jammukashmir', 'Jammu kashmir'), ('Punjab', 'Punjab'), ('Himachalpradesh', 'Himachal pradesh'), ('Haryana', 'Haryana'), ('Uttarakhand', 'Uttarakhand'), ('Uttarpradesh', 'Uttar pradesh'), ('Rajasthan', 'Rajasthan'), ('Gujarat', 'Gujarat'), ('MadhyaPradesh', 'Madhya Pradesh'), ('Jharkhand', 'Jharkhand'), ('WestBengal', 'West Bengal'), ('Maharastra', 'Maharastra'), ('Orissa', 'Orissa'), ('Chattisgarh', 'Chattisgarh'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('TamilNadu', 'Tamil Nadu'), ('Mizoram', 'Mizoram'), ('Tripura', 'Tripura'), ('Goa', 'Goa'), ('Telangana', 'Telangana')], default='', max_length=25, null=True),
        ),
    ]