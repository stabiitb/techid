from django.db import models

# Create your models here.
from signup.models import *
from django.utils.timezone import utc

class Entered(models.Model):
	user = models.ForeignKey(User)
	enter = models.DateTimeField(auto_now_add=True)
	left = models.DateTimeField(blank=True,null=True)
	is_active = models.BooleanField(default=True)

	def get_difftime(self):
		return self.left - self.enter
