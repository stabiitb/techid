from django.db import models

# Create your models here.
from misc.models import *
from signup.models import *

class Project(models.Model):
	user = models.ForeignKey(User,related_name='user')
	name = models.CharField(max_length=255)
	short_description = models.CharField(max_length=255)
	description = models.TextField()
	link	= models.URLField(null=True,blank=True)
	team = models.ManyToManyField(User,null=True,blank=True)
	is_verified = models.BooleanField(default=False)
	club 	= models.ManyToManyField(Club)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
