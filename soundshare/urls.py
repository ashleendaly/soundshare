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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.user_login, name='login'),
                  path('login/', views.user_login, name='login'),
                  path('index/', views.index, name='index'),
                  path('signup/', views.signup, name='signup'),
                  path('upload/', views.upload, name='upload'),
                  path('music/<str:music_title>/', views.music, name='music'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
