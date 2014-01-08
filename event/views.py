from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
import datetime as dt

# Create your views here.
from event.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from registration.models import *

def viewEventIndividualPage(request,code):
	template_html="events/view.html"
	entry = IndividualEvent.objects.filter(id=code)
	register = True
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
	if entry.exists():
		return render(request,template_html,{"entry":entry[0],"eventtype":"Individual","register":register})

def viewEventTeamPage(request,code):
	template_html="events/view.html"
	entry = TeamEvent.objects.filter(id=code)
	if entry.exists():
		return render(request,template_html,{"entry":entry[0],"eventtype":"Team"})

def viewEventLecturePage(request,code):
	template_html="events/view.html"
	entry = Lecture.objects.filter(id=code)
	if entry.exists():
		return render(request,template_html,{"entry":entry[0],"eventtype":"Lecture"})

def viewEventWorkshopPage(request,code):
	template_html="events/view.html"
	entry = Workshop.objects.filter(id=code)
	if entry.exists():
		return render(request,template_html,{"entry":entry[0],"eventtype":"Workshop"})

def viewEventOtherPage(request,code):
	template_html = "events/view.html"
	entry = OtherEvent.objects.filter(id=code)
	if entry.exists():
		return render(request,template_html,{"entry":entry[0],"eventtype":"Other"})


def viewIndividual(request):
	entries=IndividualEvent.objects.filter(start_time__gte=datetime.now())
	return render(request,"events/list.html",{"ind":True,"entries":entries,"type":"individual"})

def viewTeam(request):
	entries=TeamEvent.objects.filter(start_time__gte=datetime.now())
	return render(request,"events/list.html",{"team":True,"entries":entries,"type":"team"})

def viewLecture(request):
	entries=Lecture.objects.filter(start_time__gte=datetime.now())
	return render(request,"events/list.html",{"lecture":True,"entries":entries,"type":"lecture"})

def viewWorkshop(request):
	entries = Workshop.objects.filter(start_time__gte=datetime.now())
	return render(request,"events/list.html",{"workshop":True,"entries":entries,"type":"workshop"})

def viewOther(request):
	entries =OtherEvent.objects.filter(start_time__gte=datetime.now())
	return render(request,"events/list.html",{"other":True,"entries":entries,"type":"other"})