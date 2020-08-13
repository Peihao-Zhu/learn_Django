
from django.urls import path
from  .views import blog_list,blog_detail

urlpatterns = [
    path('<int:blog_pk>',blog_detail, name='blog_detail'),
    path('',blog_list, name='blog_list')
]