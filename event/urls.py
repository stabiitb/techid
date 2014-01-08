from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^individual/(\d+)/$',"event.views.viewEventPage"),
)	