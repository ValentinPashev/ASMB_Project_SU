# Generated by Django 5.1.3 on 2024-12-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_of_campaing', models.CharField(choices=[('Local', 'Local'), ('National', 'National')], default='Local', max_length=100)),
                ('branch', models.CharField(choices=[('АСМБ София', 'АСМБ София'), ('АСМБ СУ', 'АСМБ СУ'), ('АСМБ Варна', 'АСМБ Варна'), ('АСМ Пловдив', 'АСМ Пловдив'), ('АСМБ Бургас', 'АСМБ Бургас'), ('АСМБ Плевен', 'АСМБ Плевен'), ('АСМБ Стара Загора', 'АСМБ Стара Загора')], default='АСМБ СУ', max_length=100)),
                ('number_of_days', models.IntegerField(default=0)),
                ('organizers', models.TextField(blank=True, max_length=1000, null=True)),
                ('prepared', models.TextField(blank=True, max_length=35, null=True)),
                ('attended', models.TextField(blank=True, max_length=1000, null=True)),
                ('presented', models.TextField(blank=True, max_length=350, null=True)),
                ('participated_in_preliminary_training', models.TextField(blank=True, max_length=350, null=True)),
            ],
        ),
    ]
