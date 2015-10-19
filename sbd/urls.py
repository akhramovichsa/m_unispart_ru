from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from . import views

urlpatterns = [
    url(r'^q=(?P<rq>.+)/$', views.gart, name='gart')
#    url(r'^(?P<srq>.+)/$', views.search, name='search'),
]
