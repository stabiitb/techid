from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
import datetime as dt
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound

import json
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import sys

from django import forms
from django.forms import ModelForm
from django_select2 import *

from signup.models import *
from misc.models import *

class SignupForm(ModelForm):
	department = fields.ModelChoiceField(queryset=Department.objects.all(),
		widget=Select2Widget(attrs={"style":"width:100%"}),initial=0)
	year = fields.ModelChoiceField(queryset=Year.objects.all(),
		widget=Select2Widget(attrs={"style":"width:100%"}),initial=0)
	hostel = fields.ModelChoiceField(queryset=Hostel.objects.all(),
		widget=Select2Widget(attrs={"style":"width:100%"}),initial=0)
	password = forms.CharField(widget=forms.PasswordInput())
	re_password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField(widget=forms.HiddenInput(),required=False)
	rollno = forms.CharField(widget=forms.HiddenInput(),required=False)
	class Meta:
		model = User
		exclude = ['is_active','is_admin','email','ldap_username','rollno','skill']
		fields = ['first_name','last_name','password','re_password',
		'department','year','hostel','room','alternate_email','mobile']

	def __init__(self, *args, **kwargs):
		self.email = kwargs.pop('email',False)
		self.roll = kwargs.pop('roll',False)
		super(SignupForm, self).__init__(*args, **kwargs)
		self.fields["email"].value = self.email
		self.fields["rollno"].value = self.roll

	def clean(self): # check if password 1 and password2 match each other
	    if 'password' in self.cleaned_data and 're_password' in self.cleaned_data:#check if both pass first validation
	        if self.cleaned_data['password'] != self.cleaned_data['re_password']: # check if they match each other
	            raise forms.ValidationError("passwords dont match each other")
		return self.cleaned_data

	def save(self,commit=True,*args,**kwargs): # create new user
		email = kwargs.pop('email',False)
		roll = kwargs.pop('roll',False)
		if commit:
			data = {}
			data["department"] = self.cleaned_data["department"]
			data["year"] = self.cleaned_data["year"]
			data["hostel"] = self.cleaned_data["hostel"]
			data["room"] = self.cleaned_data["room"]
			try:
				validate_email(self.cleaned_data["alternate_email"])
				data["alternate_email"] = self.cleaned_data["alternate_email"]
			except:
				data["alternate_email"]  = None
			data["mobile"] = self.cleaned_data["mobile"]
			data["ldap_username"] = email.split("@")[0]
			data["rollno"] = roll
			print self.fields["email"].value,"hhjj"
			new_user=User.objects.create_user(email=email,
		                                    first_name=self.cleaned_data['first_name'],
		                                    last_name=self.cleaned_data['last_name'],
		                                    password=self.cleaned_data['password'],is_active=False,**data)

			return new_user

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=10)

class ResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=10)
    re_password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=10)
    
class EmailForm(forms.Form):
    email = forms.EmailField(required=True)
