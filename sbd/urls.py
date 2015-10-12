from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<rq>[0-9]+)/$', views.gart, name='gart'),
    url(r'^(?P<srq>.+)/$', views.search, name='search'),
]
