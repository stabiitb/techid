from django.db import models

# Create your models here.
from misc.models import *

class Resource(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	text = models.TextField(null=True,blank=True)
	fileField = models.FileField(upload_to='documents/%Y/%m/%d')
	club = models.ForeignKey(Club)

	def __unicode__(self):
		return self.name