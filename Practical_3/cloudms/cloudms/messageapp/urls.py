#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:10:07 2023

@author: farjana
"""

from django.urls import path
from messageapp import views

urlpatterns = [
    path('',views.msgproc),
]