
from django.urls import path

from .views import aritcle_detail,article_list

urlpatterns = [
    path('<int:article_id>', aritcle_detail, name='article_detail'),
    path('',article_list, name='article_list'),

]