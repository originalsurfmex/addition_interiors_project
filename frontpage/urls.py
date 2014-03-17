from django.conf.urls import patterns, url

from frontpage import views
from frontpage.views import RelationshipList, BrandList, AboutDetail

urlpatterns = patterns('',
                       # url(r'^$', views.base_page, name='base'),
                       url(r'^$', views.home_page, name='home'),

                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^sms/$', views.sms, name='sms'),
                       url(r'^thanks/$', views.thanks, name='thanks'),
                       url(r'^relationships/$', RelationshipList.as_view(), name='relationship_list'),
                       url(r'^brands/$', BrandList.as_view()),
                       url(r'^about/$', AboutDetail.as_view()),

                       # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
                       )
