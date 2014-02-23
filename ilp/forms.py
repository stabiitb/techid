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

from ilp.models import *

class RegistrationForm(ModelForm):
	members = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=
			Select2MultipleWidget(attrs={"style":"width:100%"}),required=False)
	class Meta:
		model = Ilpteam
		exclude = ['program']
