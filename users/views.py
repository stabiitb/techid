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
@login_required
def view_profile(request):
	user = request.user
	return render(request,"profile.html",{"user":user})

def logout(request):
	request.session.flush()
	request.session["login"] = True
	messages.add_message(request,messages.INFO,"You have been logged out")
	return HttpResponseRedirect("/")

@login_required
def edit_profile(request):
	if request.method == "GET":
		form = EditForm()
		return render(request,"edit.html",{"form":EditForm(instance=request.user)})
	elif request.method == "POST":
		form = EditForm(request.POST,request.FILES,instance=request.user)
		if form.is_valid():
			info=form.save(commit=False)
			form.save_m2m()
			info.save()
			messages.add_message(request,messages.INFO,"Updated succesfully")
			return HttpResponseRedirect("/edit/profile/")
		else:
			messages.add_message(request,messages.ERROR,"error Updating your details")
			return render(request,"edit.html",{"form":EditForm(instance=request.user)})