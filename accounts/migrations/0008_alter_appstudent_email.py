# Generated by Django 5.1.3 on 2024-12-11 08:53

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_activity_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appstudent',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[accounts.validators.CustomEmailValidator]),
        ),
    ]