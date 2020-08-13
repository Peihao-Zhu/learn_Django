from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #后台显示列表
    list_display = ("id","title","author","if_deleted","content","created_time","last_update_time","read_num")
    #加一个 ","表示odering是元组
    #按照id 进行正序排序
    #如果想要倒序排序 ordering = ("-id",)
    ordering = ("id",)

#admin.site.register(Article,ArticleAdmin)

