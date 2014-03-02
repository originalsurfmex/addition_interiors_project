from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addition_interiors_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^grappelli/', include('grappelli.urls')), #grappelli urls
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('frontpage.urls', namespace='frontpage'))
    #url(r'^$', 'frontpage.views.home', name='home'),
)
