# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect

def viewMessagesForm(request):
	return render(request,'messages.html')

def viewMessage(request):
	return render(request,'viewMessage.html')