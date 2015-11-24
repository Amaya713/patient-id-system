# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:26:45 2015

@author: Abhishektha
"""

from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.init, name = 'init'),
	url(r'^patient/new/$', views.patient_new, name = 'patient_new'),
	url(r'^patient/edit/$', views.patient_edit, name = 'patient_edit'),
	url(r'^patient/view/$', views.patient_view, name = 'patient_view'),
]