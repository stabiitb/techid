from django.db import models

# Create your models here.

class Students(models.Model):
	rollno = models.CharField(max_length=14,unique=True,blank=False)
	name = models.CharField(max_length=50)
	ldapid = models.CharField(max_length=30,unique=True,blank=False)
	hostel = models.IntegerField()
	dept   = models.CharField(max_length=20)
	room   = models.IntegerField()
	year   = models.CharField(max_length=6)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	picture = models.CharField(max_length=67)

	@classmethod
	def isexists(cls,ldapid):
		if len(Students.objects.filter(ldapid=ldapid)) > 0:#----- "select COUNT(*) as cnt from Students where ldapid='" + ldapid + "'";
			return True
		else:
			return False

	@classmethod
	def isexistsId(cls,lid):
		if len(Students.objects.filter(id=lid)) > 0:#----- "select COUNT(*) as cnt from Students where ldapid='" + ldapid + "'";
			return True
		else:
			return False
	
