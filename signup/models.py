from django.db import models

# Create your models here.

class Students(models.Model):
	ldapid = models.CharField(max_length=30,null=False,unique=True)
	roll   = models.CharField(max_length=3,null=False,unique=True)
	