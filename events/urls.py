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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^view/$',viewReq),
    url(r'$','signup.views.index'),
    url(r'^select2/', include('django_select2.urls')),


)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
