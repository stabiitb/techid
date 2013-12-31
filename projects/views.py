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
from signup.forms import *
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.models import check_password
from django.core.validators import validate_email	
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import *
from signup.models import *
from misc.models import *
from signup.forms import *
from projects.models import *
from django.views.generic.edit import FormView
from projects.forms import *

@login_required
def new_project(request):
	if request.method == "GET":
		return render(request,"project.html",{"form":ProjectForm(),"form_name":"Create a new project"})
	else:
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			info = form.save(commit=False)
			info.user = request.user
			info.save()
			form.save_m2m()
			return HttpResponseRedirect("/myprojects")
		else:
			messages.add_message(request,messages.ERROR,"Error creating the form")
			return render(request,"project.html",{"form":form,"form_name":"Create a new project"})

@login_required
def edit_project(request,code):
	user = request.user
	try:
		project = Project.objects.get(id=code,user=user)
	except Excpetion,e:
		return HttpResponseRedirect("/myprojects")
	if request.method == "GET":
		return render(request,"project.html",{"form":ProjectForm(instance=project),
			"form_name":"Edit project"})
	elif request.method =="POST":
		form = ProjectForm(request.POST,request.FILES,instance=project)
		if form.is_valid():
			form.save(commit=False)
			form.save_m2m()
			return HttpResponseRedirect("/myprojects")
		else:
			messages.add_message(request,messages.ERROR,"Error creating the form")
			return render(request,"project.html",{"form":form,"form_name":"Create a new project"})

@login_required
def delete_project(request,code):
	pass
class ProjectView(FormView):
    template_name = 'project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        return super(ProjectView, self).form_valid(form)