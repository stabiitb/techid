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
		if request.session.get("login"):
			request.session["login"]=False
			return render(request,"index.html",
			{"form":form,"login":True})
		return render(request,"index.html",
			{"form":form})
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


def activate(request,code,email):
	code = code
	email = email
	try:

		u = RegistrationCode.objects.get(user=User.objects.get(email=email),
			registration_code=code)
		u.delete()
		user=User.objects.get(email=email)
		user.is_active = True
		user.save()
		messages.add_message(request,messages.INFO,"Your  account is verified, Please login")
		request.session["login"] = True
		return HttpResponseRedirect("/")
	except Exception,e:
		messages.add_message(request,messages.ERROR,"wrong verification code")
		request.session["login"] = True
		return HttpResponseRedirect("/")

def reset_password(request,code):
	form_name = "Reset your Password"
	if request.method == "GET":
		try:
			r = ResetCode.objects.get(reset_code=code)
			messages.add_message(request,messages.INFO,"""Please enter a new 
				password to get access""")
			return render(request,"reset.html",{"form_name":form_name,"form":ResetForm()})
		except Exception,e:
			print e
			messages.add_message(request,messages.ERROR,"""The reset password link is invalid. 
				Please request a new one""")
			return HttpResponseRedirect("/forgot/password/")
	elif request.method == "POST":
		form = ResetForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data["password"]
			re_password = form.cleaned_data["re_password"]
			if password==re_password:
				r = ResetCode.objects.get(reset_code=code)
				user = r.user
				user.set_password(password)
				user.save()
				r.delete()
				messages.add_message(request,messages.INFO,"""Your password been reset.
					Please login with your new password """)
				request.session["login"]=True
				return HttpResponseRedirect("/")
			else:
				messages.add_message(request,messages.ERROR,"""Passwords don't match""")
				return render(request,"reset.html",{"form_name":form_name,
					"form":ResetForm()})
		else:
			return render(request,"reset.html",{"form_name":form_name,
				"form":ResetForm()})

def forgot_password(request):
	form_name = "Forgot Password"
	if request.method == "GET":
		return render(request,"reset.html",{"form_name":form_name,"form":EmailForm()})
	elif request.method == "POST":
		#check if the user exists:
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			try:
				u=User.objects.get(email=email)
			except Exception,e:
				messages.add_message(request,messages.INFO, """ We cannot find you in our database,
					Please signup""")
				return HttpResponseRedirect("/")
			try:
				r = ResetCode.objects.get(user=u)
				mail_message = "Please click on the password reset link %s"%r.reset_code
				send_mail('Subject here',mail_message, 'bila@billa.com',
					[email], fail_silently=False)
			except Exception,e:
				print e
				from signup.helper import *
				r = ResetCode(user=u,reset_code=activation_code(email))
				r.save()
				mail_message = "Please click on the password reset link %s"%r.reset_code
				send_mail('Subject here',mail_message, 'billa@billa.com',
					[email], fail_silently=False)
			messages.add_message(request,messages.INFO,"""reset link is sent to the email %s"""%email)
			return HttpResponseRedirect("/forgot/password/")
		else:
			return render(request,"reset.html",{"form_name":form_name,
				"form":form,})

def user_complete(request):
	r = User.objects.all()
	data = []
	for i in r:
		h = {}
		h["name"] = i.first_name+" "+i.last_name
		h["value"] = i.ldap_username
		h["roll"] = i.rollno
		h["tokens"] = [i.first_name,i.last_name]
		data+=[h]
	return HttpResponse(json.dumps(data,indent=4),mimetype="application/json")
