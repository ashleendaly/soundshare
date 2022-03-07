# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : urls.py
# Time       ：2022/3/7 0:36
# Author     ：Jiacheng Zhu
# version    ：python 3.9
# Description：
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
