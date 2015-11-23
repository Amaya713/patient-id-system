from django.shortcuts import render
from .models import Patient
from django.utils import timezone
from .forms import PatientForm
from django.shortcuts import redirect

# Create your views here.

def patient_list(request):
	Patients = Patient.objects.filter(edited_date=timezone.now()).order_by('edited_date')
	return render(request, 'polls/patient_list.html',{})
	
def init(request):
	return render(request, 'polls/init.html',{})
	
def patient_new(request):
	if request.method == "PATIENT":
		form = PatientForm()
		if form.is_valid():
			patient = form.save(commit=False)
			patient.author = request.user
			patient.edited_date = timezone.now()
			patient.save()
			return redirect('polls.init')
	else:
		form = PatientForm()
		
	return render(request, 'polls/patient_new.html',{'form':form})