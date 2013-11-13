from django.db import models
from signup.models import *
# Create your models here.
import hashlib
from django.core.exceptions import ValidationError
class Users(models.Model):
	username=models.CharField(max_length=255,unique=True)
	password=models.CharField(max_length=12)
	email_address=models.EmailField()
	verification_code = models.CharField(max_length=255)

	def __unicode__(self):
		return self.username

	def save(self,*args,**kwargs):
		h = hashlib.new('ripemd160')
		h.update(self.username+" "+self.password)
		self.verification_code = h.hexdigest()
		super(Users, self).save(*args, **kwargs)

	@classmethod
	def isexists(cls,username):
		if len(cls.objects.filter(username=username)) > 0:
			return True
		else:
			return False

class Has(models.Model):
	username = models.ForeignKey(Users)
	rollno = models.ForeignKey(Students)

class Unauthenticated_users(models.Model):
	username = models.CharField(max_length=255,unique=True)
	email_address = models.EmailField()
	rollno = models.CharField(max_length=14)
	verification_code = models.CharField(max_length=255)

	def save(self,*args,**kwargs):
		if len(Users.objects.filter(username=self.username)) > 0:
			raise ValidationError('Username already Exist!!')
		else:	
			h = hashlib.new('ripemd160')
			h.update(self.username+" "+self.email_address+" salt")
			self.verification_code = h.hexdigest()
			models.Model.save(self, *args, **kwargs)
			super(Unauthenticated_users, self).save(*args, **kwargs)

	def getCode(self):
		return self.verification_code
	@classmethod
	def isexists(cls,username):
		if len(cls.objects.filter(username=username)) > 0:
			return True
		else:
			return False



class dept(models.Model):
	dept_small = models.CharField(max_length=10)
	dept_fullname= models.CharField(max_length=50)

	def getFullname(self,dept_small):
		l1 = dept.objects.filter(dept_small=dept_small)
		if len(l1) > 0:
			return False
		else:
			return l1[0].dept_fullname
