from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$','tinkerer.views.tinkererlogs'),
	url(r'enter/$','tinkerer.views.timeEnter'),
	url(r'leave/$','tinkerer.views.timesubmit'),
	url(r'components/$','tinkerer.views.table_view'),
	)
