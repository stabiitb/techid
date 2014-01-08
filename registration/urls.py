from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^individual/view/(\d+)/$','registration.views.viewAllIndividual'),
	url(r'^individual/(\d+)/$','registration.views.registerIndividual'),
	url(r'^individual/deregister/(\d+)/$','registration.views.deregisterIndividual'),
	url(r'^lecture/view/(\d+)/$','registration.views.viewAllLecture'),
	url(r'^lecture/(\d+)/$','registration.views.registerLecture'),
	url(r'^lecture/deregister/(\d+)/$','registration.views.deregisterLecture'),
	url(r'^workshop/(\d+)/$','registration.views.registerWorkshop'),
	url(r'^workshop/deregister/(\d+)/$','registration.views.deregisterWorkshop'),
)