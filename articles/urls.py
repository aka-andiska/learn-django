from django.conf.urls import url
from django.contrib import admin

from .views import article_list
from .views import article_create
from .views import article_detail
from .views import article_update
from .views import article_delete

urlpatterns = [
	url(r'^$', article_list, name='list'),
    url(r'^create/$', article_create),
    url(r'^(?P<slug>[\w-]+)/$', article_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', article_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', article_delete),
    #url(r'^articles/$', "<appname>.views.<function_name>"),
]
