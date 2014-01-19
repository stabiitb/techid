from django.contrib import admin

# Register your models here.
from event.models import *
from image_cropping import ImageCroppingMixin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from suit_redactor.widgets import RedactorWidget
from django_select2 import *
from django.forms import TextInput, ModelForm, Textarea, Select
from misc.models import *
from django import forms

class EventForm(ModelForm):
	class Meta:
		widgets={
		'dept_elligible':Select2MultipleWidget(attrs={"style":"width:100%"}),
		'year_elligible':Select2MultipleWidget(attrs={"style":"width:100%"}),
		'hostel_elligible':Select2MultipleWidget(attrs={"style":"width:100%"}),
		'conducted_by':Select2MultipleWidget(attrs={"style":"width:100%"}),
		'description':RedactorWidget(editor_options={'lang': 'en'}),
		'special_notes':RedactorWidget(editor_options={'lang': 'en'}),
		'venue':Select2Widget(attrs={"style":"width:100%"}),
		'end_note':RedactorWidget(editor_options={'lang': 'en'}),
		'other_notes':RedactorWidget(editor_options={'lang': 'en'}),
		}

class EventAdmin(ImageCroppingMixin,admin.ModelAdmin):
	form = EventForm


from tinkerer.models import *
from registration.models import *
from projects.models import *
from resources.models import *
admin.site.register(Entered)
admin.site.register(Component)
admin.site.register(Resource)
admin.site.register(Project)
admin.site.register(IndividualRegistration)
admin.site.register(TeamEvent,EventAdmin)
admin.site.register(IndividualEvent,EventAdmin)
admin.site.register(Lecture,EventAdmin)
admin.site.register(Workshop,EventAdmin)
admin.site.register(OtherEvent,EventAdmin)
