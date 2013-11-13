from django.db import models
from signup.models import *
from event.models import *
from users.models import *
# Create your models here.
class Teams(models.Model):
	teamname = models.CharField(max_length=60)


class Registerd(models.Model):
	sid = models.ManyToManyField(Students)
	eid = models.ManyToManyField(Competition)

class Formed(models.Model):
	teamid = models.ForeignKey(Teams)
	sid = models.ManyToManyField(Students)	

class TeamRegistered(models.Model):
	teamid = models.ForeignKey(Teams)
	eventid = models.ForeignKey(TeamEvent)

