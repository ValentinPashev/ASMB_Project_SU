# Generated by Django 5.1.3 on 2024-12-08 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.CharField(default=4, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            preserve_default=False,
        ),
    ]
