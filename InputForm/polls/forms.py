# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 01:05:04 2015

@author: Abhishektha
"""

from django import forms
from .models import Patient

YESNO = (
	(True,'Yes'),
	(False,'No')
)

class PatientForm(forms.ModelForm):
	
	class Meta:
		model = Patient
		fields = ('title','DOB','Allergies','ProcedureName','Eye','Lens','SetforDistance','Near','Lensx','ORA','IStent')
	