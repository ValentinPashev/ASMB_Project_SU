# Generated by Django 5.1.3 on 2024-12-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaing',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]