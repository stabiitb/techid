from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^individual/$','event.views.viewIndividual'),
	url(r'^team/$','event.views.viewTeam'),
	url(r'^lecture/$','event.views.viewLecture'),
	url(r'^workshop/$','event.views.viewWorkshop'),
	url(r'^otherevent/$','event.views.viewOther'),
	url(r'^individual/(\d+)/$',"event.views.viewEventIndividualPage"),
	url(r'^team/(\d+)/$',"event.views.viewEventTeamPage"),
	url(r'^lecture/(\d+)/$',"event.views.viewEventLecturePage"),
	url(r'^workshop/(\d+)/$',"event.views.viewEventWorkshopPage"),
	url(r'^otherevent/(\d+)/$',"event.views.viewEventOtherPage"),

)	