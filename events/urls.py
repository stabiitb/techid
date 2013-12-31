from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from users.views import *
from registration.views import *
from signup.views import *
from event.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'events.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^view/$',viewReq),
    url(r'^signup/1/$','signup.views.check_signup'),
    url(r'^signup/$','signup.views.signup'),
    url(r'^$','signup.views.index'),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^activate/(?P<code>\w+)/(?P<email>[a-zA-Z0-9_.@-]+)/$','signup.views.activate'),
    url(r'^reset/password/(?P<code>\w+)/$','signup.views.reset_password'),
    url(r'^forgot/password/$',"signup.views.forgot_password"),
    url(r'^user.json/$','signup.views.user_complete'),
    url(r'^profile/$','users.views.view_profile'),
    url(r'^logout/$','users.views.logout'),
    url(r'^edit/profile/$','users.views.edit_profile'),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
