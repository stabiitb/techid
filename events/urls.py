from django.conf.urls import patterns, include, url

from django.contrib import admin
from event.views import index,viewCreateEvent,createEvent,viewEventPage,viewEvents
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from users.views import login,signup_stage1,viewProfile,editProfile
from messages.views import *
from signup.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'events.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup/1/$',signup_stage1),
    url(r'^event/cult/(\d+)/$',viewEvents),
    url(r'^event/(\d+)/$',viewEventPage),
    url(r'^users/(\d+)/$',viewProfile),
    url(r'^create/event/$',viewCreateEvent),
    url(r'^create/event/new$',createEvent),
    url(r'^$','event.views.index',name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'^messages/$',viewMessagesForm),
    url(r'^messages/view/sent/$',viewMessage),
    url(r'^users/edit/$',editProfile),
    url(r'^signup/2/$',signupHandler),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
