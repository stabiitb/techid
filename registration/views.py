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
from signup.mail import *
@login_required
def registerIndividual(request,code):
	template = "emails/thankyou.txt"
	subject = "[Event Registration] Confirmation:"
	from_email = "stab.iitb@gmail.com"
	to_email = request.user.email
	url = "http://techid.stab-iitb.org/"+"events/individual/"
	try:
		event =IndividualEvent.objects.get(id=code)
		entry=IndividualRegistration.objects.filter(user=request.user,
			event=IndividualEvent.objects.get(id=code))
		if entry.exists():
			messages.add_message(request,messages.ERROR,"unable to register you")
		else:
			IndividualRegistration.objects.create(user=request.user,
				event=IndividualEvent.objects.get(id=code))
			try:
				data = {"username":request.user.first_name,"url":url+str(event.id)}
				send_email(template,subject,from_email,to_email,data)
			except Exception,e:
				print e
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

def viewAllLecture(request,code):
	register = True
	entry = Lecture.objects.filter(id=code)
	try:
		user = request.user
		i = LectureRegistration.objects.filter(user=user,event=entry[0])
		print i
		if i.exists():
			register = False
		else:
			register = True
	except Exception,e:
		pass

	try:
		entries=LectureRegistration.objects.filter(event=Lecture.objects.get(id=code))
		if entries.exists():
			return render(request,"events/registered.html",{"registered":entries,
				"eventtype":"Lecture","entry":Lecture.objects.get(id=code),
				"register":register})
	except Exception:
		pass
	return render(request,"events/registered.html",
			{"eventtype":"Lecture",
			"entry":Lecture.objects.get(id=code),"register":register})

def viewAllWorkshop(request,code):
	register = True
	entry = Workshop.objects.filter(id=code)
	try:
		user = request.user
		i = WorkshopRegistration.objects.filter(user=user,event=entry[0])
		print i
		if i.exists():
			register = False
		else:
			register = True
	except Exception,e:
		pass

	try:
		entries=WorkshopRegistration.objects.filter(event=Workshop.objects.get(id=code))
		if entries.exists():
			return render(request,"events/registered.html",{"registered":entries,
				"eventtype":"Workshop","entry":Workshop.objects.get(id=code),
				"register":register})
	except Exception:
		pass
	return render(request,"events/registered.html",
			{"eventtype":"Workshop",
			"entry":Workshop.objects.get(id=code),"register":register})

@login_required
def registerLecture(request,code):
	try:
		entry=LectureRegistration.objects.filter(user=request.user,
			event=Lecture.objects.get(id=code))
		if entry.exists():
			messages.add_message(request,messages.ERROR,"unable to register you")
		else:
			LectureRegistration.objects.create(user=request.user,
				event=Lecture.objects.get(id=code))
			messages.add_message(request,messages.SUCCESS,"you are successfully registerd for the event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to register you")
		
	return HttpResponseRedirect("/events/lecture/"+str(code))

@login_required
def deregisterLecture(request,code):
	try:
		i = LectureRegistration.objects.filter(user=request.user,
			event=Lecture.objects.get(id=code))
		for items in i:
			i.delete()
		messages.add_message(request,messages.SUCCESS,"you have been de registered from event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to deregister you")
		
	return HttpResponseRedirect("/events/lecture/"+str(code))

@login_required
def registerWorkshop(request,code):
	try:
		entry=WorkshopRegistration.objects.filter(user=request.user,
			event=Workshop.objects.get(id=code))
		if entry.exists():
			messages.add_message(request,messages.ERROR,"unable to register you")
		else:
			WorkshopRegistration.objects.create(user=request.user,
				event=Workshop.objects.get(id=code))
			messages.add_message(request,messages.SUCCESS,"you are successfully registerd for the event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to register you")
		
	return HttpResponseRedirect("/events/workshop/"+str(code))

@login_required
def deregisterWorkshop(request,code):
	try:
		i = WorkshopRegistration.objects.filter(user=request.user,
			event=Workshop.objects.get(id=code))
		for items in i:
			i.delete()
		messages.add_message(request,messages.SUCCESS,"you have been de registered from event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to deregister you")
		
	return HttpResponseRedirect("/events/workshop/"+str(code))


def viewAllOtherEvent(request,code):
	register = True
	entry = OtherEvent.objects.filter(id=code)
	try:
		user = request.user
		i = OtherEventRegistration.objects.filter(user=user,event=entry[0])
		print i
		if i.exists():
			register = False
		else:
			register = True
	except Exception,e:
		pass

	try:
		entries=OtherEventRegistration.objects.filter(event=OtherEvent.objects.get(id=code))
		if entries.exists():
			return render(request,"events/registered.html",{"registered":entries,
				"eventtype":"OtherEvent","entry":OtherEvent.objects.get(id=code),
				"register":register})
	except Exception:
		pass
	return render(request,"events/registered.html",
			{"eventtype":"OtherEvent",
			"entry":OtherEvent.objects.get(id=code),"register":register})


@login_required
def registerOtherEvent(request,code):
	try:
		entry=OtherEventRegistration.objects.filter(user=request.user,
			event=OtherEvent.objects.get(id=code))
		if entry.exists():
			messages.add_message(request,messages.ERROR,"unable to register you")
		else:
			OtherEventRegistration.objects.create(user=request.user,
				event=OtherEvent.objects.get(id=code))
			messages.add_message(request,messages.SUCCESS,"you are successfully registerd for the event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to register you")
		
	return HttpResponseRedirect("/events/otherevent/"+str(code))

@login_required
def deregisterOtherEvent(request,code):
	try:
		i = OtherEventRegistration.objects.filter(user=request.user,
			event=OtherEvent.objects.get(id=code))
		for items in i:
			i.delete()
		messages.add_message(request,messages.SUCCESS,"you have been de registered from event")
	except Exception,e:
		print e
		messages.add_message(request,messages.ERROR,"unable to deregister you")
		
	return HttpResponseRedirect("/events/otherevent/"+str(code))
