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
from season.models import *
from ilp.models import *

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


def send_an_email(modeladmin, request, queryset):
    pass

send_an_email.short_description = "Send an email"

class EventAdmin(ImageCroppingMixin,admin.ModelAdmin):
	list_display = ('id','name','venue','start_time',)
	search_fields = ('name',)
	form = EventForm

class RegistrationAdmin(admin.ModelAdmin):
	list_filter = ('event',)
	actions = [send_an_email]

class ProgramForm(ModelForm):
	class Meta:
		widgets = {
		'details':RedactorWidget(editor_options={'lang': 'en'}),
		}
class IlpTeamForm(ModelForm):
	members = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=
			Select2MultipleWidget(attrs={"style":"width:100%"}),required=False)
	class Meta:
		pass
class ProgramAdmin(ImageCroppingMixin,admin.ModelAdmin):
	list_display = ('title','attachements')
	form = ProgramForm

class IlpTeamAdmin(ImageCroppingMixin,admin.ModelAdmin):
	list_display = ('team_name','program')
	form = IlpTeamForm

from tinkerer.models import *
from registration.models import *
from projects.models import *
from resources.models import *

admin.site.register(Program,ProgramAdmin)
admin.site.register(Ilpteam,IlpTeamAdmin)
admin.site.register(Video)
admin.site.register(Entered)
admin.site.register(Component)
admin.site.register(Resource)
admin.site.register(Project)
admin.site.register(IndividualRegistration,RegistrationAdmin)
admin.site.register(LectureRegistration,RegistrationAdmin)
admin.site.register(WorkshopRegistration,RegistrationAdmin)
admin.site.register(OtherEventRegistration,RegistrationAdmin)

admin.site.register(TeamEvent,EventAdmin)
admin.site.register(IndividualEvent,EventAdmin)
admin.site.register(Lecture,EventAdmin)
admin.site.register(Workshop,EventAdmin)
admin.site.register(OtherEvent,EventAdmin)
