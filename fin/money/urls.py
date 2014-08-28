from django.conf.urls.defaults import *

from money import views

urlpatterns = patterns('',
	url('all', views.all, name='all'),
	url('add', views.add, name='add'),
	url(r'^$', views.index, name='index'),
)
