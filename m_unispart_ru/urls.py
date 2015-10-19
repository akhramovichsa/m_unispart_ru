from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from m_unispart_ru import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'm_unispart_ru.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^else/$', TemplateView.as_view(template_name="else.html"), name='else'),
                       url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^search/$',    TemplateView.as_view(template_name="search.html"), name='search'),
                       url(r'^gart/', include('sbd.urls')),
                       )
