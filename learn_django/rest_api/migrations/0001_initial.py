# Generated by Django 3.1 on 2020-10-10 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(default=datetime.datetime(2020, 10, 10, 15, 14, 2, 1955, tzinfo=utc))),
                ('sex', models.CharField(max_length=5)),
            ],
        ),
    ]
