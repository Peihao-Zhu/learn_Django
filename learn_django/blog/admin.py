from django.contrib import admin
from .models import BlogType,Blog

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    # 后台显示列表
    list_display = ("id",  "type_name")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 后台显示列表
    list_display = ("id", "title", "author", "blog_type", "content", "created_time", "last_updated_time")