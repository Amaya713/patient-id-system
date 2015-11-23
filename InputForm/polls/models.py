from django.db import models
from django.utils import timezone
#import datetime
#from django.db import timezone
# Create your models here.

EYES = (
	('L','left'),
	('R','Right'),
)

PROCEDURE_NAMES = (
	('cs','cataract surgery'),
	('t','trabeculectomy'),
	('cst','cataract surgery/trabeculectomy'),
	('a','Ahmed Valve'),
	('ce','Chalazio excison'),
	('rdr','Retinal Detachment repair'),
	('emp','Epiretinal Membrane peel'),
	('v','vitrectormy'),
)

SETFOROP = (
	('Distance','Distance'),
	('Near','Near'),
)

SETFOR = (
	('-1.90','-1.90'),
	('-1.25','-1.25'),
	('-1.50','-1.50'),
	('-1.75','-1.75'),
	('-2.00','-2.00'),
	('-2.25','-2.25'),
	('-2.50','-2.50'),
)

YESNO = (
	('Yes','Yes'),
	('No','No')
)


class Patient(models.Model):
	author = models.ForeignKey('auth.User')
	edited_date = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=200)
	DOB = models.DateField(default=timezone.now)
	Allergies = models.TextField()
	ProcedureName = models.CharField(max_length=200, choices = PROCEDURE_NAMES)
	Eye = models.CharField(max_length=2, choices = EYES)
	Lens = models.CharField(max_length=200)
	SetforDistance = models.CharField(max_length=200, choices = SETFOROP)
	Near = models.CharField(max_length=200, choices = SETFOR)
	Lensx = models.BooleanField()
	ORA = models.BooleanField()
	IStent = models.BooleanField()
	Power = models.CharField(max_length=200)
	Comments = models.TextField()
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
	

	