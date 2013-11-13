# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from messages.models import *
from signup.models import *
from users.models import *
def viewMessagesForm(request):
	if 'p' in request.GET:
		p = request.GET['p']
		if p== 'error':
			return render(request,'messages.html')
		elif p != 'error':
			return render(request,'messages.html',{'username':p})
		else:
			return render(request,'messages.html')
	else:
		return render(request,'messages.html')

def viewMessage(request):
	return render(request,'viewMessage.html')

def createMessage(request):
	if 'user' not in request.session:
		return HttpResponseRedirect("/")
	elif 'username' in request.POST and 'message' in request.POST:
		username = request.POST['username']
		message = request.POST['message']
		myname= request.session['user']
		if Users.isexists(username):
			m1 = Messages(data=message,sent_id=Users.objects.filter(username=myname)[0],received_id=Users.objects.filter(username=username)[0])
			m1.save()
			return HttpResponseRedirect("/messages/received/")
		else:
			return HttpResponseRedirect("/messages?p=error")
def viewRMessages(request):
	if 'user' not in request.session:
		return HttpResponseRedirect("/")
	else:
		username = request.session['user']
		m1 = Messages.objects.filter(received_id=Users.objects.filter(username=username)[0])[::-1]
		return render(request,'viewMessage.html',{'rec':True,'reco':m1,'sent':True})

def viewSMessages(request):
	if 'user' not in request.session:
		return HttpResponseRedirect("/")
	else:
		username = request.session['user']
		m1 = Messages.objects.filter(sent_id=Users.objects.filter(username=username)[0])[::-1]
		return render(request,'viewMessage.html',{'rec':False,'reco':m1,'sent':True})

def forwardMessages(request):
	if 'user' not in request.session:
		return HttpResponseRedirect("/")
	else:
		if 'p' in request.GET:
			p = request.GET['p']
			m1 = Messages.objects.filter(id=p)[0]
			m1 = "--Forwarded From "+m1.sent_id.username+"--\n"+m1.data
			return render(request,'messages.html',{'m':m1})
		else:
			return HttpResponseRedirect("/")