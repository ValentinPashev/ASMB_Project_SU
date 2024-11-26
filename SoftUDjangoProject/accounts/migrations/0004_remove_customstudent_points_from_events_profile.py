# Generated by Django 5.1.3 on 2024-11-25 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customstudent_points_from_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customstudent',
            name='points_from_events',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('faculty_number', models.CharField(default='', max_length=25, unique=True)),
                ('branch', models.CharField(choices=[('АСМБ МУ', 'АСМБ МУ'), ('АСМБ СУ', 'АСМБ СУ'), ('АСМБ Варна', 'АСМБ Варна'), ('АСМБ Пловдив', 'АСМБ Пловдив'), ('АСМБ Бургас', 'АСМБ Бургас'), ('АСМБ Плевен', 'АСМБ Плевен'), ('АСМБ Стара Загора', 'АСМБ Стара Загора')], default='АСМБ СУ', max_length=25)),
                ('points_from_events', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
