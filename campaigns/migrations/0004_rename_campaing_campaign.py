# Generated by Django 5.1.3 on 2024-12-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_campaing_points_for_attended_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Campaing',
            new_name='Campaign',
        ),
    ]
