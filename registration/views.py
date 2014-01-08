# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.core.mail import send_mail
import json
import urllib
import urllib2,cookielib
import requests
from users.models import *
from signup.models import *
from registration.models import *
from event.models import *
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.models import check_password
from django.core.validators import validate_email	
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import *

@login_required

def registerIndividual(request,code):
	try:
		entry=IndividualRegistration.objects.filter(user=request.user,
			event=IndividualEvent.objects.get(id=code))
		if entry.exists():
			messages.add_message(request,messages.ERROR,"unable to register you")
		else:
			IndividualRegistration.objects.create(user=request.user,
				event=IndividualEvent.objects.get(id=code))
			messages.add_message(request,messages.SUCCESS,"you are successfully registerd for the event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to register you")
		
	return HttpResponseRedirect("/events/individual/"+str(code))

@login_required
def deregisterIndividual(request,code):
	try:
		i = IndividualRegistration.objects.filter(user=request.user,
			event=IndividualEvent.objects.get(id=code))
		for items in i:
			i.delete()
		messages.add_message(request,messages.SUCCESS,"you have been de registered from event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to deregister you")
		
	return HttpResponseRedirect("/events/individual/"+str(code))


def viewAllIndividual(request,code):
	register = True
	entry = IndividualEvent.objects.filter(id=code)
	try:
		user = request.user
		i = IndividualRegistration.objects.filter(user=user,event=entry[0])
		print i
		if i.exists():
			register = False
		else:
			register = True
	except Exception,e:
		pass

	try:
		entries=IndividualRegistration.objects.filter(event=IndividualEvent.objects.get(id=code))
		if entries.exists():
			return render(request,"events/registered.html",{"registered":entries,
				"eventtype":"Individual","entry":IndividualEvent.objects.get(id=code),
				"register":register})
	except Exception:
		pass
	return render(request,"events/registered.html",
			{"eventtype":"Individual",
			"entry":IndividualEvent.objects.get(id=code),"register":register})