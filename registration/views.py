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

