from django.db import models

from django.db import models
from signup.models import *
from event.models import *
from users.models import *
# Create your models here.
class Video(models.Model):
	name = models.CharField(max_length=255)
	html_code = models.TextField()
	link = models.URLField(null=True,blank=True)
	club = models.ForeignKey(Club)
	videoFile = models.FileField(upload_to='videos/%Y/%m/%d',null=True,blank=True)

	def __unicode__(self):
		return self.name
