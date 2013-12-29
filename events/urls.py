from django.conf.urls import patterns, include, url

from django.contrib import admin
from event.views import *
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from users.views import *
from registration.views import *
from signup.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'events.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^filebrowser/', include('filebrowser.urls')),
    url(r'^verify/new/$',newPassword),
    url(r'^verify/$',verify),
    url(r'^signup/1/$',signup_stage1),
    url(r'^events/all/$',viewEvents),
    url(r'^event/(\d+)/$',viewEventPage),
    url(r'^users/(\d+)/$',viewProfile),
    url(r'^create/event/$',viewCreateEvent),
    url(r'^create/event/new$',createEvent),
    url(r'^$','event.views.index',name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'^users/edit/$',editProfile),
    url(r'^signup/2/$',signupHandler),
    url(r'^event/register/$',IndividualRegistration),
    url(r'^logout/$',logout),
    url(r'^view/$',viewReq),
    url(r'^select2/', include('django_select2.urls')),


)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
