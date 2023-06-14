#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:24:55 2023

@author: farjana
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello),
]