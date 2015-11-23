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
	#title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-area', 'placeholder': 'Enter patients name'}), required = True)	
	#allergies = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-area', 'placeholder': 'Enter patient allergies'}), required = False)	
	
	class Meta:
		model = Patient
		fields = ('title','DOB','Allergies','ProcedureName','Eye','Lens','SetforDistance','Near','Lensx','ORA','IStent')
		#fields = ('title','DOB')