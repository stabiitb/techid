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
from projects.models import *
from django.views.generic.edit import FormView
from projects.forms import *

def new_project(request):
	return render(request,"project.html",{"form":ProjectForm()})

class ProjectView(FormView):
    template_name = 'project.html'
    form_class = ProjectForm

    def form_valid(self, form):
        return super(ProjectView, self).form_valid(form)