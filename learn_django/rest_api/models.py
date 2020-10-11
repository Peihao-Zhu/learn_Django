

from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20) #和数据库相关的字段，char类型
    content = models.TextField(null=True)
    created_time = models.DateTimeField(default=timezone.now(), null=True)
    sex = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = 'user'
