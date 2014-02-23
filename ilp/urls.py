from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$','ilp.views.viewAllProjects'),
	url(r'^(\d+)/$',"ilp.views.viewProject"),
)