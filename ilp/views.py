from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
import datetime as dt

# Create your views here.
from ilp.models import *
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
from signup.models import *
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.models import check_password
from django.core.validators import validate_email	
from django.contrib.auth.decorators import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import *

@login_required
def viewAllProjects(request):
	template_html = "ilp/all.html"
	entries = Program.objects.all()
	return render(request,template_html,{"entries":entries})

@login_required
def viewProject(request,id):
	template_html = "ilp/page.html"
	is_entry = Program.objects.filter(id=id)
	if is_entry.exists():
		return render(request,template_html,{"entry":entry})
	else:
		raise Http404

