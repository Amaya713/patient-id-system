# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:26:45 2015

@author: Abhishektha
"""

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.patient_list, name = 'patient_list'),
]