from django.db import models

# Create your models here.
class Users(models.Model):
	username=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	email_address=models.EmailField()
	verification_code = models.CharField(max_length=255)

	def __unicode__(self):
		return self.username