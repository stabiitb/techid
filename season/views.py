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
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.models import check_password
from django.core.validators import validate_email	
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import *
from signup.mail import *
from season.models import *

def viewall(request):
	entries = Video.objects.all()
	return render(request,"seasons/viewall.html",{"entries":entries})