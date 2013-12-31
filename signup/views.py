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
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.models import check_password
from django.core.validators import validate_email	
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import *

##function to get the detials of the user:
def getValues(ldap_id):
	url = "http://www.cse.iitb.ac.in/~prithvirajbilla/ldap-api/?user="+ldap_id
	req = urllib2.Request(url)
	response = urllib2.urlopen(req,)
	the_page = response.read()
	array = json.loads(the_page)
	return array

@require_http_methods(["GET","POST"])
def index(request):
	form_name = "Login Here with you email"
	if request.method == "GET":
		form = LoginForm()
		return render(request,"index.html",
			{"form":form,"login":True})
	elif request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			try:
				k= User.objects.get(email=email)
			except Exception,e:
				messages.add_message(request,messages.ERROR,
					"Please signup to get an user account")
				return render(request,"index.html",{"form":form,"login":True})
			check =k.check_password(password)
			if k is not None and check:
				if k.is_active:
					user = authenticate(email=email,password=password)
					login(request,user)
					return HttpResponseRedirect("/profile/")
				else:
					messages.add_message(request,messages.INFO,
						"Please  confirm your registration,we already have your email in our database")
					return render(request,"index.html",{"form":form,"login":True})
			elif k is None:
				messages.add_message(request,messages.ERROR,
					"Please signup to get an user account")
				return render(request,"index.html",{"form":form,"login":True})
			else:
				messages.add_message(request,messages.ERROR,
					"Passwords did not match")
				return render(request,"index.html",{"form":form,"login":True})

		else:
			return render(request,"index.html",{"form":form,"login":True})


def signup(request):
	if request.method == "GET":
		if request.session.get("email") and request.session.get("roll"):
			form =SignupForm(initial={"first_name":request.session["first_name"],
				"last_name":request.session["last_name"]})
			return render(request,"signup.html",{"form":form,"session":request.session})
		else:
			messages.add_message(request,messages.ERROR,"The page you tried to acces doesn't exist")
		return HttpResponseRedirect("/")
	elif request.method == "POST":
		if request.session.get("email") and request.session.get("roll"):
			form = SignupForm(request.POST,email=request.session["email"],roll=request.session["roll"])
			email = request.session["email"]
			try:
				u=User.objects.get(email=email)
				if u.is_active:
					messages.add_message(request,messages.ERROR,"""Account with this email 
						already exists and activated.If you forgot the password,click forgot password""")
				else:
					messages.add_message(request,messages.ERROR,""""Your account is not activated, 
						please click the link to send the activation link again to your email""")
				return HttpResponseRedirect("/")
			except Exception,e:
				print e
				pass
			if form.is_valid():

				mail = request.session["email"]
				d= {}
				d["email"]=mail
				d["roll"]=request.session["roll"]
				user=form.save(commit=True,**d)
				from signup.helper import *
				code = activation_code(request.session["email"])
				r=RegistrationCode(user=user,
					registration_code=code)
				r.save()
				mail_message  = "click on this registration link"
				mail_message += code + "/" +mail 
				try:
					send_mail('Registraion Link',mail_message, 
						'billa@billa.com',
	    				[mail], fail_silently=True)
				except Exception,e:
					print e
					pass
				messages.add_message(request,messages.INFO,"Registration activation link is sent to your email")
				return HttpResponseRedirect("/signup")
			else:
				return render(request,"signup.html",{"form":form,"session":request.session})
		else:
			messages.add_message(request,messages.ERROR,"The page you tried to acces doesn't exist")
		return HttpResponseRedirect("/")

@require_http_methods(["GET"])
def check_signup(request):
	if "email" in request.GET:
		email = request.GET["email"]
		try:
			validate_email(email)
		except Exception,e:
			messages.add_message(request,messages.ERROR,"please type a valid email")
			return HttpResponseRedirect("/")
		try:
			u=User.objects.get(email=email)
			if u.is_active:
				messages.add_message(request,messages.ERROR,"""Account with this email 
					already exists and activated.If you forgot the password,click forgot password""")
			else:
				messages.add_message(request,messages.ERROR,""""Your account is not activated, 
					please click the link to send the activation link again to your email""")
			return HttpResponseRedirect("/")
		except Exception,e:
			username = email.split("@")[0]
			if email.split("@")[1] != "iitb.ac.in":
				messages.add_message(request,messages.ERROR,"""This portal is only for IITB-ians""")
				return HttpResponseRedirect("/")
			data = getValues(username)
			if 'error' in data:
				messages.add_message(request,messages.ERROR,"""Ldap account doesn't exist""")
				return HttpResponseRedirect("/")
			else:
				request.session["email"] = email
				request.session["roll"] = data["rollno"]
				request.session["first_name"] = data["fname"]
				request.session["last_name"] = data["lname"]
				return HttpResponseRedirect("/signup")
	else:
		return HttpResponseRedirect("/")