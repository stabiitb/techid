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
	form = EditForm()
	return render(request,"edit.html",{"form":EditForm()})