from django.db import models

# Create your models here.
from misc.models import *
from image_cropping import ImageRatioField
class Event(models.Model):
	name = models.CharField(max_length=255)
	description =models.TextField()
	venue = models.ForeignKey(Venue)
	start_time = models.DateTimeField()
	duration = models.CharField(max_length=255,null=True,blank=True)
	year_elligible = models.ManyToManyField(Year,default=Year.objects.all())
	dept_elligible = models.ManyToManyField(Department)
	hostel_elligible = models.ManyToManyField(Hostel,default=Hostel.objects.all())
	picture = models.ImageField(max_length=100,upload_to='documents/%Y/%m/%d',blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	attachements = models.FileField(max_length=100,upload_to='documents/%Y/%m/%d',blank=True,null=True)
	end_note	= models.TextField(null=True,blank=True)
	special_notes = models.TextField(null=True,blank=True)
	conducted_by= models.ManyToManyField(Club)
	ended		= models.BooleanField(default=False)
	cropping = ImageRatioField('picture', '1024x300',size_warning=True)
	small_cropping = ImageRatioField('picture','200x200',size_warning=True)
	@classmethod
	def isexists(cls,eventid):
		if len(cls.objects.filter(id=eventid)) > 0:
			return True
		else:
			return False

	def __unicode__(self):
		return self.name

class TeamEvent(Event):
	deadline_to_register = models.DateTimeField(null=True,blank=True)
	team_size			 = models.IntegerField(null=True,blank=True,default=0)
	submission			 = models.BooleanField(default=False)
	submission_on		= models.DateTimeField(null=True,blank=True)
	other_notes	= models.TextField(null=True,blank=True)

class IndividualEvent(Event):
	deadline_to_register = models.DateTimeField(null=True,blank=True)
	submission = models.BooleanField(default=False)
	submission_on		= models.DateTimeField(null=True,blank=True)
	other_notes	= models.TextField(null=True,blank=True)


class Lecture(Event):
	topic			 = models.CharField(max_length=255)
	other_notes 	= models.TextField(null=True,blank=True)

class Workshop(Event):
	deadline_to_register = models.DateTimeField(null=True,blank=True)
	workshop_on	= models.CharField(max_length=255)
	other_notes = models.TextField(null=True,blank=True)

class OtherEvent(Event):
	other_notes = models.TextField(null=True,blank=True)