from django.conf.urls import patterns, include, url
from django.contrib import admin

#this is for django 1.6 - remove for 1.7:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addition_interiors_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')), #grappelli urls
    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^$', include('frontpage.urls', namespace='frontpage'))
)
