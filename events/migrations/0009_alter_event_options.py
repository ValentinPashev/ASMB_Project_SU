# Generated by Django 5.1.3 on 2024-12-11 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_eventreport_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': [('can_approve_events', 'Can approve event'), ('can_make_report', 'Can make report'), ('can_see_report', 'Can see report'), ('can_edit_report', 'Can edit report')]},
        ),
    ]
