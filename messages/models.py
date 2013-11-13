from django.db import models
from users.models import *
from signup.models import *
# Create your models here.
class Messages(models.Model):
	data = models.CharField(max_length=320)
	timestamp = models.DateTimeField(auto_now_add=True)
	sent_id = models.ForeignKey(Users)
	received_id = models.ForeignKey(Users,related_name='messages_recieved_id')
