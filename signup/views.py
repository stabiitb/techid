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
		year = request.POST['year']
		if Students.isexists(ldapid):
			return HttpResponseRedirect("/signup/1/?p=already")
		elif Users.isexists(username):
			return HttpResponseRedirect("/signup/1/?p=error")
		elif Unauthenticated_users.isexists(username):
			return HttpResponseRedirect("/signup/1/?p=usernameExists")
		else:
			if 'rollno' not in array:
				return HttpResponseRedirect("/")
			un1 = Unauthenticated_users(username=username,email_address=ldapid+"@iitb.ac.in",rollno=array['rollno'])
			un1.save()
			s1 = Students(name=name,rollno=array['rollno'],ldapid=array['ldapid'],hostel=hostel,room=room,dept=array['dept'],email=ldapid+"@iitb.ac.in",phone=phone,year=year)
			s1.save()
			send_mail('Verification Code[event manager]', 'Hello\n, Welcome to our site. To activat your account, your activation code is'+un1.getCode(), 'from@example.com',['to@example.com'], fail_silently=False)
			return HttpResponseRedirect("/verify")
	else:
		return HttpResponseRedirect("/signup/1/?p=error1")


def verify(request):
	if 'p' in request.GET:
		p = request.GET['p']
		## got a vefication code:
		un_object = Unauthenticated_users.objects.filter(verification_code=p)
		if len(un_object) > 0:
			username = un_object[0].username
			email_address = un_object[0].email_address
			request.session['verification'] = p
			request.session['signup_username'] = username
			request.session['email_address'] = email_address
			request.session['rollno'] = un_object[0].rollno
			return render(request,'forgotpassword.html',{'forgot':False})
		else:
			return render(request,'verify.html',{'error':True})
	else:
		return render(request,"verify.html")

def newPassword(request):
	if 'password' in request.POST and 'repassword' in request.POST:
		password = request.POST['password']
		repassword = request.POST['repassword']
		if password == repassword:
			if 'verification' in request.session:
				p = request.session['verification']
				username = request.session['signup_username']
				email_address = request.session['email_address']
				rollno = request.session['rollno']
				u1 = Users(username=username,email_address=email_address,password=password)
				u1.save()
				s1 = Students.objects.filter(rollno=rollno)[0]
				h1 = Has(username=u1,rollno=s1)
				h1.save()
				del request.session['verification']
				del request.session['signup_username']
				del request.session['email_address']
				request.session.modified = True
				request.session['user'] = username
				request.session['rollno'] = rollno
				return HttpResponseRedirect("/users/"+str(s1.id))
			else:
				return HttpResponseRedirect("/verify?p=error")
		else:
			return HttpResponseRedirect("/verify?p="+request.session['verification'])
	else:
		return HttpResponseRedirect("/")