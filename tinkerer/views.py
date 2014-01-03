from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from tinkerer.forms import *
from tinkerer.models import *
from signup.models import *
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib import messages

@login_required
def tinkererlogs(request):
	template_html = "tinkerer/new.html"
	if Entered.objects.filter(user=request.user).exists():
		entries = Entered.objects.filter(user=request.user,is_active=False)
		totaltime = sum(us.left - us.enter  for us in entries)
		return render(request,template_html,{"entries":entries,"totaltime":totaltime})
	else:
		messages.add_message(request,messages.INFO,"No logs for tinkerer's lab yet")
		return render(request,template_html)

@login_required
def timesubmit(request):
	if Entered.objects.filter(user=request.user,is_active=True).exists():
		entry=Entered.objects.filter(user=request.user)[0]
		entry.is_active = False
		entry.left = datetime.now()
		entry.save()
		messages.add_message(request,messages.INFO,"You have been signed out from Tinkerer's lab")
		return HttpResponseRedirect("/tinkerer/")
	else:
		messages.add_message(request,messages.INFO,"you have already been signed out from Tinkerer's Lab")
		return HttpResponseRedirect("/tinkerer/")	


@login_required
def timeEnter(request):
	if Entered.objects.filter(user=request.user,is_active=True).exists():
		messages.add_message(request,messages.INFO,"you have already been signed up in Tinkerer's Lab")
		return HttpResponseRedirect("/tinkerer/")
	else:
		Entered.objects.create(user=request.user)
		messages.add_message(request,messages.INFO,"you have signed into Tinkerer's lab")
		return HttpResponseRedirect("/tinkerer")
