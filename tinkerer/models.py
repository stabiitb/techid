from django.db import models

# Create your models here.
from signup.models import *
from django.utils.timezone import utc

class Entered(models.Model):
	user = models.ForeignKey(User)
	enter = models.DateTimeField(auto_now_add=True)
	left = models.DateTimeField(blank=True,null=True)
	is_active = models.BooleanField(default=True)
	purpose = models.TextField(max_length=500)
	def get_difftime(self):
		return self.left - self.enter

	def __unicode__(self):
		return self.user.email

class Component(models.Model):
	CHOICES=(
		("MODULES","Modules"),
		("RESISTORS","Resistors"),
		("POTENTIOMETER","Potentiometer"),
		("CAPACITORS","Capactors"),
		("PROCESSOR","Processors"),
		("Logic Gate","Logic gates"),
		("General purpose","General purpose"),
		("SENSORS","sensors"),
		("CONNECTORS","connectors"),
		("SEMICONDUCTORS","semiconductors"),
		)

	idNo = models.CharField(max_length=255,verbose_name="id no")
	name = models.CharField(max_length=255)
	url = models.URLField(blank=True,null=True)
	number = models.CharField(max_length=255)
	typeOfComponent = models.CharField(max_length=255,choices=CHOICES)

