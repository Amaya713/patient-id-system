from django.db import models
from django.utils import timezone
#import datetime
#from django.db import timezone
# Create your models here.

class Patient(models.Model):
	author = models.ForeignKey('auth.User')
	edited_date = models.DateTimeField(default=timezone.now)
	Name = models.CharField(max_length=200)
	DOB = models.CharField(max_length=200)
	Allergies = models.TextField()
	ProcedureName = models.CharField(max_length=200)
	Eye = models.CharField(max_length=2)
	Lens = models.CharField(max_length=200)
	Setfor = models.CharField(max_length=200)
	Lensx = models.CharField(max_length=200)
	Power = models.CharField(max_length=200)
	Comments = models.TextField()
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
	

	