#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls.py
   Description :
   Author :       Administrator
   date：          2019/4/23 14:31
-------------------------------------------------
   Change Activity:
                   14:31:
-------------------------------------------------
"""
__author__ = 'Administrator'
from django.urls import path
from . import  views
urlpatterns= [
    path('',views.index,name='index')
]