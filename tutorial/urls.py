"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static



schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include('snippets.urls')),
    url(r'^comments/', include("comments.urls", namespace='comments')),

    url(r'^', include("articles.urls", namespace='articles')),
    url(r'^api/articles/', include("articles.api.urls", namespace='articles-api')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]


