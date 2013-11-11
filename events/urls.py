from django.conf.urls import patterns, include, url

from django.contrib import admin
from event.views import index,viewEvent,createEvent,viewEventPage
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from users.views import login,signup_stage1

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'events.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup/1/$',signup_stage1),
    url(r'^event/(\d+)/$',viewEventPage),
    url(r'^create/event/$',viewEvent),
    url(r'^create/event/new$',createEvent),
    url(r'^$','event.views.index',name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
