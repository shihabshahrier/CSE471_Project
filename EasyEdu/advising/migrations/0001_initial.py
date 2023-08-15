# Generated by Django 4.2.3 on 2023-08-12 17:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreAdvising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advising_day', models.DateField(default=datetime.date.today)),
                ('advising_start_time', models.TimeField(default=datetime.time)),
                ('advising_end_time', models.TimeField(default=datetime.time)),
                ('session', models.CharField(default='Fall 2021', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAdvising',
            fields=[
                ('advising_id', models.AutoField(primary_key=True, serialize=False)),
                ('advising_day', models.DateField(default=datetime.date.today)),
                ('advising_start_time', models.TimeField(default=datetime.time)),
                ('advising_end_time', models.TimeField(default=datetime.time)),
                ('session', models.CharField(default='Fall 2021', max_length=10)),
                ('credit', models.IntegerField(default=0)),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
            ],
        ),
    ]