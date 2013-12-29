from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
import datetime as dt
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound

import json
from django.core.exceptions import ValidationError

import sys

from django import forms
from django.forms import ModelForm
from django_select2 import *

from signup.models import *
from misc.models import *

class SignupForm(ModelForm):
	class Meta:
		model = User
		exclude = ['is_active','is_admin','email','ldap_username','rollno']
		fields = ['first_name','last_name','department','year','hostel','room','alternate_email','mobile','skill']
		widgets = {
		'department' :Select2Widget(attrs={"style":"width:100%"}),
		'year':Select2Widget(attrs={"style":"width:100%"}),
		'hostel':Select2Widget(attrs={"style":"width:100%"}),
		}
		
class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=10)

