from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#DJANGO-FILEBROWSER
from filebrowser.sites import site

from frontpage import views


#this is for django 1.6 - remove for 1.7:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), #grappelli urls
    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
    #---------- APPS ----------#    
    url(r'', include('frontpage.urls', namespace='frontpage')),
) 

#SERVE STATIC FILES::NOT RECOMMENDED!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


#FOR DJANGO-DEBUG-TOOLBAR
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),   
    )
