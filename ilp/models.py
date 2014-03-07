from django.db import models
from signup.models import *
# Create your models here.
from image_cropping import ImageRatioField

class Program(models.Model):
	title = models.CharField(max_length=255)
	attachements = models.FileField(max_length=100,upload_to='documents/ilp/%Y/%m/%d',blank=True,null=True)
	details = models.TextField(null=True,blank=True)
	team_size = models.IntegerField()
	other_details = models.TextField(null=True,blank=True)
	picture = models.ImageField(max_length=100,upload_to='documents/%Y/%m/%d',blank=True,null=True)
	small_cropping = ImageRatioField('picture','200x200',size_warning=True)
	company_name = models.CharField(max_length=255)
	link	= models.URLField(null=True,blank=True)
	def __unicode__(self):
		return self.title

class Ilpteam(models.Model):
	team_name = models.CharField(max_length=255)
	program = models.ForeignKey(Program)
	members = models.ManyToManyField(User)
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.team_name
