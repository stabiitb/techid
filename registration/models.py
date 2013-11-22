from django.db import models
from signup.models import *
from event.models import *
from users.models import *
# Create your models here.
class Teams(models.Model):
	teamname = models.CharField(max_length=60)

	@classmethod
	def isexists(cls,tid):
		if len(cls.objects.filter(id=tid)) == 0:
			return False
		else:
			return True
			
class Registered(models.Model):
	sid = models.ForeignKey(Students)
	eid = models.ForeignKey(Event)

class Formed(models.Model):
	teamid = models.ForeignKey(Teams)
	sid = models.ForeignKey(Students)
	@classmethod
	def AlreadyFormed(cls,teamname,sid):
		if len(Teams.objects.filter(teamname=teamname)) == 0:
			return False
		else:
			if len(cls.objects.filter(teamid=Teams.objects.filter(teamname=teamname)[0]),sid=Students.objects.filter(sid=sid)[0]) == 0:
				return False
			else:
				return True

class TeamRegistered(models.Model):
	teamid = models.ForeignKey(Teams)
	eventid = models.ForeignKey(Event)

