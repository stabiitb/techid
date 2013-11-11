from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
# Create your views here.
import json
import urllib
import urllib2,cookielib
import requests
from users.models import Users
def login(request):
	if 'username' in request.POST and 'password' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		if len(Users.objects.filter(username=username,password=password)) == 0:
			return HttpResponseRedirect('/?p=error')
		else:
			request.session['user'] = username
			return render(request,'index.html')
	else:
		return HttpResponseRedirect('/')

def signup_stage1(request):
	if 'email' in request.POST:
		email = request.POST['email']
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
		url = "http://www.cse.iitb.ac.in/~prithvirajbilla/ldap-api/?user="+ldap_id
		req = urllib2.Request(url,headers=hdr)
		response = urllib2.urlopen(req,)
		the_page = response.read()
		array = json.loads(the_page)
		if 'ldap_id' in array:
			return render(request,'signup.html',{'ldap_id':array['ldap_id']})
		else:
			return HttpResponseRedirect("/")
	else:
		return render(request,'signup.html')