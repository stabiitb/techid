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
from signup.forms import *
##function to get the detials of the user:
def getValues(ldap_id):
	url = "http://www.cse.iitb.ac.in/~prithvirajbilla/ldap-api/?user="+ldap_id
	req = urllib2.Request(url)
	response = urllib2.urlopen(req,)
	the_page = response.read()
	array = json.loads(the_page)
	return array

def index(request):
	form = LoginForm()
	return render(request,"index.html",{"form":form})