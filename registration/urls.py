from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^individual/view/(\d+)/$','registration.views.viewAllIndividual'),
	url(r'^individual/(\d+)/$','registration.views.registerIndividual'),
	url(r'^individual/deregister/(\d+)/$','registration.views.deregisterIndividual'),
)