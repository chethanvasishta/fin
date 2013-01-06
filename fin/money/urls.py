from django.conf.urls.defaults import *

from money import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
