# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/28 23:05'

from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)