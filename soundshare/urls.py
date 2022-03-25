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
                  path('forgetpassword/', views.forget_password, name='forget_password'),
                  path('logout/', views.user_logout, name='logout'),
                  path('index/', views.index, name='index'),
                  path('signup/', views.signup, name='signup'),
                  path('upload/', views.music_upload, name='upload'),
                  path('music_search/', views.music_search, name='music_search'),
                  path('music/', views.music_all, name='music'),
                  path('music/<str:music_title>/', views.music, name='music'),
                  path('music/<str:music_title>/add_like/', views.add_like, name='add_like'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
