from django.db import models
from  django.utils import timezone
from  django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    #title 和content是数据库对应的属性
    title=models.CharField(max_length=30) #和数据库相关的字段，char类型
    content=models.TextField()
    created_time=models.DateTimeField(default=timezone.now())
    #每次更新字段，都会更新这个时间
    last_update_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    if_deleted=models.BooleanField(default=False)
    read_num=models.IntegerField(default=0)

    def __str__(self):
        return "<Article:%s>" % self.title