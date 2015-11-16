from django.shortcuts import render
from .models import Patient
from django.utils import timezone

# Create your views here.

def patient_list(request):
	Patients = Patient.objects.filter(edited_date=timezone.now()).order_by('edited_date')
	return render(request, 'blog/patient_list.html',{})
	