# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/28 17:56'

from django.urls import path

from .views import post_list, post_detail, post_new, post_edit


app_name = 'blog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:post_id>/edit/', post_edit, name='post_edit'),
]