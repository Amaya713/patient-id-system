from django.shortcuts import render
from .models import Patient
from django.utils import timezone
from .forms import PatientForm
from django.shortcuts import redirect
#from django.http import HttpResponse

# Create your views here.

def patient_view(request):
	patients = Patient.objects.filter(edited_date__lte=timezone.now()).order_by('edited_date')
	return render(request, 'polls/patient_list.html',{'patients':patients})
	
def init(request):
	return render(request, 'polls/init.html',{})

def patient_new(request):
	form = PatientForm()
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid():
			Patient = form.save(commit=False)
			Patient.author = request.user
			Patient.edited_date = timezone.now()
			Patient.save()
			return redirect('polls.views.init')
		else:
			print form.errors
	else:
		form = PatientForm()
	return render(request, 'polls/patient_new.html',{'form':form})

def patient_edit(request):
	form = PatientForm()
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid():
			Patient = form.save(commit=False)
			Patient.author = request.user
			Patient.edited_date = timezone.now()
			Patient.save()
			return redirect('polls.views.init')
		else:
			print form.errors
	else:
		form = PatientForm()
	return render(request, 'polls/patient_edit.html',{'form':form})
