from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
import datetime as dt

# Create your views here.
from ilp.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from signup.models import *
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.models import check_password
from django.core.validators import validate_email	
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import *
from ilp.forms import *

@login_required
def viewAllProjects(request):
	template_html = "ilp/all.html"
	entries = Program.objects.all()
	return render(request,template_html,{"entries":entries})

@login_required
def viewProject(request,id):
	template_html = "ilp/page.html"
	is_entry = Program.objects.filter(id=id)
	if is_entry.exists():
		return render(request,template_html,{"entry":is_entry[0]})
	else:
		raise Http404

@login_required
def register(request,id):
	template_html="ilp/register.html"
	template = "emails/ilp.txt"
	subject = "Mail confirmation for ILP"
	form = RegistrationForm()
	from_email = "stab.iitb@gmail.com"
	to_email = request.user.email
	url = "http://techid.stab-iitb.org/"+"ilp/"
	is_entry = Program.objects.filter(id=id)
	if is_entry.exists():
		program = is_entry[0];
		if request.method == "GET":
			try:
				ilpteam = Ilpteam.objects.filter(program=program,members__in=[request.user])
				form = RegistrationForm(instance=ilpteam[0])
				return render(request,template_html,{"entry":is_entry[0],"form":form})
			except Exception,e:
				print e
				return render(request,template_html,{"entry":is_entry[0],"form":form})
		else:
			ilpteam = Ilpteam.objects.filter(program=program,members__in=[request.user])
			awesome = False
			if ilpteam.exists():
				form = RegistrationForm(request.POST,instance=ilpteam[0])
			else:
				if unicode(request.user.id) not in request.POST.getlist('members'):
					print request.POST.getlist('members')
					awesome = True
				form = RegistrationForm(request.POST)

			if form.is_valid():
				if len(request.POST.getlist('members')) > program.team_size:
					messages.add_message(request,messages.ERROR,"You cannot add more than "+str(program.team_size)+" members")
					return HttpResponseRedirect("/ilp/register/"+str(program.id))
				info=form.save(commit=False)
				info.program = program
				info_id=info.save()
				form_id=form.save_m2m()
				if  awesome:
					info.members.add(request.user)
				messages.add_message(request,messages.INFO,"Added your detials")
			else:
				messages.add_message(request,messages.ERROR,"error Adding your details")
			try:
				data = {"username":request.user.first_name,"url":url+str(program.id)}
				send_email(template,subject,from_email,to_email,data)
			except Exception,e:
				pass

			return HttpResponseRedirect("/ilp/register/"+str(program.id))

	else:
		raise Http404

@login_required
def registered(request,id):
	template_html="ilp/registered.html"
	is_entry = Program.objects.filter(id=id)
	if is_entry.exists():
		teams = Ilpteam.objects.filter(program=is_entry[0])
		return render(request,template_html,{"entry":is_entry[0],"teams":teams,"registered":True})
	else:
		raise Http404
