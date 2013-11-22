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

def IndividualRegistration(request):
	if 'eventid' in request.POST:
		eventid = request.POST['eventid']
		if 'id' in request.session:
			sid = request.session['id']
			if Event.isexists(eventid) and Students.isexistsId(sid):
				if len(Registered.objects.filter(sid=Students.objects.filter(id=sid)[0],eid=Event.objects.filter(id=eventid))) == 0:
					r1 = Registered(sid=Students.objects.filter(id=sid)[0],eid=Event.objects.filter(id=eventid)[0])
					r1.save()
					return HttpResponseRedirect("/event/"+str(eventid)+"/?p=success")
				else:
					return HttpResponseRedirect("/event/"+str(eventid)+"/?p=already")
			else:
				return HttpResponseRedirect("/event/"+str(eventid)+"/?p=error")
		else:
			return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")

def TeamRegistration(request):
	if 'id' in request.session and 'eventid' in request.POST: 
		sid = request.session['id']
		eventid = request.POST['eventid']
		if Event.isexists(eventid) and Students.isexistsId(sid):
			if 'teamname' in request.POST:
				teamname = request.POST['teamname']
				if Formed.AlreadyFormed(teamname,sid):
					return HttpResponseRedirect("/event/"+str(eventid)+"/?p=already")
				else:
					t=Teams(teamname=teamname)
					t.save()
					f=Formed(teamid=t,sid=Students.objects.filter(id=sid)[0])
					f.save()
					tr = TeamRegistered(teamid=t,eventid=Event.objects.filter(id=eventid)[0])
					tr.save()
					return HttpResponseRedirect("/even/"+str(eventid)+"/?p=success")
			elif 'teamid' in request.POST:
				teamid = request.POST['teamid']
				if Teams.isexists(teamid):
					sid = request.session['id']
					tid = Teams.objects.filter(id=teamid)[0]
					if len(Formed.objects.filter(teamid=tid,sid=Students.objects.filter(sid)[0])) == 0:
						f = Formed(teamid=tid,sid=Students.objects.filter(sid)[0])
						f.save()
						return HttpResponseRedirect("/even/"+str(eventid)+"/?p=success")
				else:
					return HttpResponseNotFound("<h4>Something is wrong</h4>")
		else:
			return HttpResponseRedirect("/event/"+str(eventid)+"/?p=already")
	else:
		return HttpResponseNotFound("<h4>Something is wrong</h4>")