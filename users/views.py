from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
import json
import urllib
import urllib2,cookielib
import requests
from users.models import *
from signup.models import *
def login(request):
	if 'username' in request.POST and 'password' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		if len(Users.objects.filter(username=username,password=password)) == 0:
			return HttpResponseRedirect('/?p=error')
		else:
			request.session['user'] = username
			h1 = Has.objects.filter(username=Users.objects.filter(username=username)[0])[0]
			s1 = h1.rollno.id
			request.session['id'] = s1
			request.session['roll'] = h1.rollno.rollno
			return HttpResponseRedirect("/users/"+str(s1))	
	else:
		return HttpResponseRedirect('/')

def signup_stage1(request):
	if 'email' in request.GET:
		email = request.GET['email']
		ldap_id = (email.split("@"))[0]
		proxy_support = urllib2.ProxyHandler({'http':'http://rajeev_kumar:+eragonxxx*@netmon.iitb.ac.in:80',
                                               'https':'https://rajeev_kumar:eragonxxx*@netmon.iitb.ac.in:80'})
		opener = urllib2.build_opener(proxy_support)
		urllib2.install_opener(opener)
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       			'Accept-Encoding': 'none',
       			'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
		url = "http://localhost/ldap-api/?user="+ldap_id
		req = urllib2.Request(url,headers=hdr)
		response = urllib2.urlopen(req,)
		the_page = response.read()
		array = json.loads(the_page)
		print array
		if 'ldapid' in array:
			return render(request,'signup.html',{'ldapid':array['ldapid'],'roll':array['rollno'],'dept':array['dept'],'name':array['fname']+" "+array['lname']})
		else:
			return HttpResponseRedirect("/?p=signup")
	elif 'p' in request.GET:
		p = request.GET['p']
		if p=='error':
			return render(request,'signup.html',{'error':True})
		elif p=='already':
			return render(request,'signup.html',{'error2':True})
		elif p=='usernameExists':
			return render(request,'signup.html',{'error3':True})
		else:
			return render(request,'signup.html')
	else:
		return HttpResponseRedirect("/")

def viewProfile(request,offset):
	if 'user' in request.session:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		s1 = Students.objects.filter(id=offset)
		if len(s1) == 0:
			raise Http404
		else:
			return render(request,'profile.html',{'student':s1[0]})
	else:		
		return HttpResponseRedirect("/")

def editProfile(request):
	if 'user' in request.session and 'rollno' in request.session:
		sid = request.session['id']
		username = request.session['user']
		rollno = request.session['roll']
		s1 = Students.objects.filter(rollno=rollno)[0]
		
		return render(request,'edit.html',{'student':s1})
	else:
		raise Http404