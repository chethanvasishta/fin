from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fin.views.home', name='home'),
    # url(r'^fin/', include('fin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    	url(r'^admin/', include(admin.site.urls)),
	url(r'^money/', include('money.urls')),
)
