# Generated by Django 4.2.3 on 2023-07-10 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time',
            field=models.TimeField(default=datetime.time(7, 52, 22, 937571)),
        ),
    ]
