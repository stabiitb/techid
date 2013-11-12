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

##function to get the detials of the user:
def getValues(ldap_id):
	url = "http://localhost/ldap-api/?user="+ldap_id
	req = urllib2.Request(url)
	response = urllib2.urlopen(req,)
	the_page = response.read()
	array = json.loads(the_page)
	return array

def signupHandler(request):
	if 'username' in request.POST and 'ldapid' in request.POST and 'name' in request.POST and 'hostel' in request.POST and 'room' in request.POST:
		array = getValues(request.POST['ldapid'])
		username = request.POST['username']
		ldapid = request.POST['ldapid']
		name = request.POST['name']
		hostel = request.POST['hostel']
		room = request.POST['room']
		phone = request.POST.get('phone',False)
		if Users.isexists(username):
			return HttpResponseRedirect("/signup/1/?p=error")
		elif Unauthenticated_users.isexists(username):
			return HttpResponseRedirect("/signup/1/?p=usernameExists")
		elif Students.isexists(ldapid):
			return HttpResponseRedirect("/signup/1/?p=already")
		else:
			un1 = Unauthenticated_users(username=username,email_address=ldapid+"@iitb.ac.in")
			un1.save()
			s1 = Students(name=name,rollno=array['rollno'],ldapid=array['ldapid'],hostel=hostel,room=room,email=ldapid+"@iitb.ac.in",phone=phone)
			s1.save()
			send_mail('Verification Code[event manager]', 'Hello\n, Welcome to our site. To activat your account, your activation code is'+un1.getCode(), 'from@example.com',['to@example.com'], fail_silently=False)
			return HttpResponseRedirect("/verify")
	else:
		return HttpResponseRedirect("/signup/1/?p=error1")


def verify(request):
	if 'p' in request.GET:
		p = request.GET['p']
		## got a vefication code:
		un_object = Unauthenticated_users.objects.filter(Verification_code=p)
		if len(un_object) > 0:
			username = un_object[0].username
			email_address = un_object[0].email_address
			request.session['verification'] = p
			request.session['signup_username'] = username
			return render(request,'forgotpassword.html',{'forgot':False})
		else:
			return HttpResponseRedirect("/verify?p=error")
	else:
		return render(request,"veify.html")
