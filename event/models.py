from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=255)
	description =models.TextField()
	venue = models.CharField(max_length=255)
	start_time = models.DateTimeField()
	duration = models.CharField(max_length=255)
	year_elligible = models.CharField(max_length=25)
	dept_elligible = models.IntegerField(default=0)
	hostel_elligible = models.IntegerField()
	picture = models.CharField(max_length=25)

	@classmethod
	def isexists(cls,eventid):
		if len(cls.objects.filter(id=eventid)) > 0:
			return True
		else:
			return False

class Concert(models.Model):
    concert = models.ForeignKey(Event)
    concertby = models.CharField(max_length=255)

class Workshop(models.Model):
	workshop = models.ForeignKey(Event)
	conductedby = models.CharField(max_length=255)
	field = models.CharField(max_length=255)

class Lecture(models.Model):
	lecture = models.ForeignKey(Event)
	speaker = models.CharField(max_length=255)

class TeamEvent(models.Model):
	teamevent = models.ForeignKey(Event)
	deadline = models.DateTimeField()
	teamsize = models.IntegerField()

class Competition(models.Model):
	competition = models.ForeignKey(Event)
	deadline = models.DateTimeField()

class CultEvent(models.Model):
	cultevent = models.ForeignKey(Event)

class TechEvent(models.Model):
	techevent = models.ForeignKey(Event)

class SportEvent(models.Model):
	sportevent = models.ForeignKey(Event)