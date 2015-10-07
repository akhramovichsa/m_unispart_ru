from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from m_unispart_ru import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'm_unispart_ru.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',          TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^contacts/$', TemplateView.as_view(template_name="contacts.html"), name='contacts'),
    url(r'^search/$',   views.search, name='search'),

    url(r'^admin/', include(admin.site.urls)),
)
