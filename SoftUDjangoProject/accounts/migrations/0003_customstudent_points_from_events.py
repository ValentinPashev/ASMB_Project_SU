# Generated by Django 5.1.3 on 2024-11-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customstudent_points_customstudent_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customstudent',
            name='points_from_events',
            field=models.IntegerField(default=0),
        ),
    ]