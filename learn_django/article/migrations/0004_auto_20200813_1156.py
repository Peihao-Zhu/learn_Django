# Generated by Django 3.1 on 2020-08-13 11:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200813_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 11, 56, 5, 592124, tzinfo=utc)),
        ),
    ]
