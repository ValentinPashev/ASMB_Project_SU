# Generated by Django 5.1.3 on 2024-11-27 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': [('can_approve_events', 'Can approve event')]},
        ),
    ]