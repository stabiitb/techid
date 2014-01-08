from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
import datetime as dt

# Create your views here.
from event.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from registration.models import *

def viewEventPage(request,code):
	template_html="events/view.html"
	entry = IndividualEvent.objects.filter(id=code)
	return render(request,template_html,{"entry":entry})