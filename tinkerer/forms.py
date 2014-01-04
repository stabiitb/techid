from django import forms
from tinkerer.models import *
from bootstrap3_datetime.widgets import DateTimePicker

class SignOutForm(forms.Form):
	left = forms.DateTimeField(required=False, label="Leaving Time",
		widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
		"pickSeconds": False},attrs={"placeholder":"Not required"}))
