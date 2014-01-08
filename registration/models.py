from django.db import models
from signup.models import *
from event.models import *
from users.models import *
# Create your models here.
class IndividualRegistration(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(IndividualEvent)

	class Meta:
		unique_together=('user','event')

	def __unicode__(self):
		return self.user.email+" | "+self.event.name