# Generated by Django 3.1 on 2020-10-11 09:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20201011_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 11, 9, 16, 23, 14021, tzinfo=utc), null=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
