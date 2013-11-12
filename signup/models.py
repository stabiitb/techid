from django.db import models

# Create your models here.

class Students(models.Model):
	rollno = models.CharField(max_length=14,unique=True,blank=False)
	name = models.CharField(max_length=50)
	ldapid = models.CharField(max_length=30,unique=True,blank=False)
	hostel = models.IntegerField()
	#dept   = models.IntegerField()
	room   = models.IntegerField()
	year   = models.CharField(max_length=6)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	picture = models.CharField(max_length=67)

	@classmethod
	def isexists(cls,ldapid):
		if len(Students.objects.filter(ldapid=ldapid)) > 0:
			return True
		else:
			return False
