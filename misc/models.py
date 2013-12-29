from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(unique=True,max_length=255)
	short_name = models.CharField(max_length=10)

class Year(models.Model):
	name = models.CharField(unique=True,max_length=255)
	short_name = models.CharField(max_length=10)

class Venue(models.Model):
	name = models.CharField(unique=True,max_length=255)
	description = models.CharField(unique=True,max_length=255)

class Hostel(models.Model):
	name = models.CharField(unique=True,max_length=255)
	description = models.CharField(max_length=255,null=True,blank=True)

class Club(models.Model):
	name = models.CharField(unique=True,max_length=255)
	description = models.TextField(null=True,blank=True)
	image = models.ImageField(max_length=255,upload_to='documents/%Y/%m/%d',blank=True,null=True)

class Skill(models.Model):
	name = models.CharField(unique=True,max_length=255)
	