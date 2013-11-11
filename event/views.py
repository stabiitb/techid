from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
# Create your views here.
from event.models import *
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
	if 'p' in request.GET:
		p = request.GET['p']
		if p == 'error':
			return render(request,'index.html',{'error':True})
		else:
			return render(request,'index.html')
	else:
		return render(request, 'index.html')

def viewEvent(request):
	if 'p' in request.GET:
		p = request.GET['p']
		if p == 'error':
			return render(request,'createEvent.html',{'error':True})
	if 'user' in request.session:
		return render(request,'createEvent.html')
	else:
		return HttpResponseRedirect("/")	

def createEvent(request):
	if 'eventname' in request.POST and 'description' in request.POST and 'venue' in request.POST and 'picture' in request.POST and 'type' in request.POST and 'starttime' in request.POST:
		eventname = request.POST['eventname']
		description = request.POST['description']
		venue = request.POST['venue']
		picture = request.POST['picture']
		starttime = request.POST.get('starttime')
		duration = request.POST['duration']
		year = request.POST['yearellig']
		dept = request.POST['dept']
		hostel = request.POST['hostel']
		type1 = request.POST['type']
		date_object = datetime.strptime(starttime, '%m/%d/%Y %I:%M %p')
		starttime = str(date_object)
		if type1=='concert':
			if 'concertby' in request.POST:
				concertby = request.POST['concertby']
				e1 = Event(name=eventname,description=description,venue=venue,start_time=starttime,duration=duration,year_elligible=year,dept_elligible=dept,hostel_elligible=hostel,picture=picture)
				e1.save()
				c1 = Concert(concert=e1,concertby=concertby)
				c1.save()
				return HttpResponseRedirect("/event/"+str(e1.id))
			else:
				return HttpResponseRedirect("/create/event?p=error")
		elif type1=='lecture':
			if 'speaker' in request.POST:
				speaker = request.POST['speaker']
				e1 = Event(name=eventname,description=description,venue=venue,start_time=starttime,duration=duration,year_elligible=year,dept_elligible=dept,hostel_elligible=hostel,picture=picture)
				e1.save()
				l1 = Lecture(lecture=e1,speaker=speaker)
				l1.save()
				return HttpResponseRedirect("/event/"+str(e1.id))
			else:
				return HttpResponseRedirect("/create/event?p=error")
		elif type1=='workshop':
			if 'workshop-speaker' in request.POST and field in request.POST:
				workshop_speaker = request.POST['workshop-speaker']
				field = request.POST['field']
				e1 = Event(name=eventname,description=description,venue=venue,start_time=starttime,duration=duration,year_elligible=year,dept_elligible=dept,hostel_elligible=hostel,picture=picture)
				e1.save()
				w1 = Workshop(workshop=e1,conductedby=workshop_speaker,field=field)
				w1.save()
				return HttpResponseRedirect("/event/"+str(e1.id))
			else:
				return HttpResponseRedirect("/create/event?p=error")
		elif type1=='individual':
			if 'deadline' in request.POST:
				deadline = request.POST['deadline']
				date_object = datetime.strptime(deadline, '%m/%d/%Y %I:%M %p')
				deadline = str(date_object)
				e1 = Event(name=eventname,description=description,venue=venue,start_time=starttime,duration=duration,year_elligible=year,dept_elligible=dept,hostel_elligible=hostel,picture=picture)
				e1.save()
				c1 = Competition(competition=e1,deadline=deadline)
				c1.save()
				return HttpResponseRedirect("/event/"+str(e1.id))
			else:
				return HttpResponseRedirect("/create/event?p=error")
		elif type1=='team':
			if 'deadline1' in request.POST and 'teammembers' in request.POST:
				deadline = request.POST['deadline1']
				teamsize = request.POST['teammembers']
				date_object = datetime.strptime(deadline, '%m/%d/%Y %I:%M %p')
				deadline = str(date_object)
				e1 = Event(name=eventname,description=description,venue=venue,start_time=starttime,duration=duration,year_elligible=year,dept_elligible=dept,hostel_elligible=hostel,picture=picture)
				e1.save()
				t1 = TeamEvent(teamevent=e1,deadline=deadline,teamsize=teamsize)
				t1.save()
				return HttpResponseRedirect("/event/"+str(e1.id))
			else:
				return HttpResponseRedirect("/create/event?p=error")
	else:
		print "lol"
		return HttpResponseRedirect("/create/event?p=error")

def viewEventPage(request,offset):
	type1 = ""
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	if len(Event.objects.filter(id=offset)) == 0:
		return Http404()
	else:
		event = Event.objects.filter(id=offset)[0]
		if len(Concert.objects.filter(concert=event)) != 0:
			concert = Concert.objects.filter(concert=event)[0]
			type1="concert"
			return render(request,'eventpage.html',{'event':event,"type":type1,'concert':concert})
		elif len(Lecture.objects.filter(lecture=event)) != 0:
			lecture = Lecture.objects.filter(lecture=event)[0]
			type1="lecture"
			return render(request,'eventpage.html',{'event':event,'type':type1,'lecture':lecture})
		elif len(Competition.objects.filter(competition=event)) != 0:
			competition = Competition.objects.filter(competition=event)[0]
			type1 = "competition"
			return render(request,'eventpage.html',{'event':event,'type':type1,'competition':competition})
		elif len(TeamEvent.objects.filter(teamevent=event)) != 0:
			teamevent = TeamEvent.objects.filter(teamevent=event)[0]
			type1 = "team"
			return render(request,'eventpage.html',{'event':event,'type':type1,'team':teamevent})
		elif len(Workshop.objects.filter(workshop=event)) != 0:
			workshop = Workshop.objects.filter(workshop=event)[0]
			type1 = "workshop"
			return render(request,'eventpage.html',{'event':event,'type':type1,'workshop':workshop})
		else:
			return render(request,'eventpage.html',{'event':event})