from django.conf.urls import patterns, url

from frontpage import views

urlpatterns = patterns('',
					   # url(r'^$', views.base_page, name='base'),
                       url(r'^$', views.home_page, name='home'),
                       # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
                       )
