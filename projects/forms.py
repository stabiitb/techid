from django.contrib import admin

# Register your models here.
from event.models import *

from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, ModelForm, Textarea, Select
from django import forms

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import sys

from django.forms import ModelForm
from django_select2 import *

from signup.models import *
from misc.models import *
from projects.models import *
from redactor.widgets import RedactorEditor

import bleach

from django.conf import settings

class ProjectForm(ModelForm):
	team = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=
		Select2MultipleWidget(attrs={"style":"width:100%"}))
	class Meta:
		model = Project
		exclude = ['is_verified','created_at','updated_at','user']
		widgets = {
		'description':RedactorEditor(redactor_options={'lang': 'en', 'focus': 'true'}),
		'club':Select2MultipleWidget(attrs={"style":"width:100%"}),
		}

	def clean_description(self):
		description = self.cleaned_data.get('description', '')
		cleaned_text = bleach.clean(description, settings.BLEACH_VALID_TAGS,
         settings.BLEACH_VALID_ATTRS, settings.BLEACH_VALID_STYLES)
		return cleaned_text #sanitize html