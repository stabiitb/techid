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
from datetime import datetime

@login_required
def tinkererlogs(request):
	template_html = "tinkerer/new.html"
	form = SignOutForm()
	if Entered.objects.filter(user=request.user,is_active=True).exists():
		if Entered.objects.filter(user=request.user).exists():
			entries = Entered.objects.filter(user=request.user,is_active=False)
			totaltime = sum(us.left - us.enter  for us in entries)
			return render(request,template_html,{"entries":entries,"totaltime":totaltime,"form":form,
				"active":True})
		else:
			messages.add_message(request,messages.INFO,"No logs for tinkerer's lab yet")
			return render(request,template_html,{"form":form,"active":True})
	else:
		if Entered.objects.filter(user=request.user).exists():
			entries = Entered.objects.filter(user=request.user,is_active=False)
			totaltime = 0
			return render(request,template_html,{"entries":entries,"totaltime":totaltime,"form":form})
		else:
			messages.add_message(request,messages.INFO,"No logs for tinkerer's lab yet")
			return render(request,template_html,{"form":form})

@login_required
def timesubmit(request):
	if Entered.objects.filter(user=request.user,is_active=True).exists():
		form = SignOutForm(request.POST)
		dt = ""
		entry=Entered.objects.filter(user=request.user)[0]
		if form.is_valid():
			print form.cleaned_data["left"]
			if form.cleaned_data["left"] == None:
				dt = datetime.now()
			else:
				if entry.enter < datetime(form.cleaned_data["left"]) \
				 and datetime(form.cleaned_data["left"]) < datetime.now():
					dt = form.cleaned_data["left"]
				else:
					messages.add_message(request,messages.ERROR,""""Left time should be greater than 
						entered time""")
					return HttpResponseRedirect("/tinkerer/")
		else:
			dt = datetime.now()

		entry.is_active = False
		entry.left = dt
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
