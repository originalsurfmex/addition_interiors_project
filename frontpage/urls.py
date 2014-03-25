from django.conf.urls import patterns, url

from frontpage import views
from frontpage.views import SkillsList, RelationshipList, BrandList, AboutDetail

urlpatterns = patterns('',
                       url(r'^$', views.home_page, name='home'),

                       url(r'^thanks/$', views.thanks, name='thanks'),

                       url(r'^skills/$', SkillsList.as_view(), name='skills-list'),

                       url(r'^relationships/$', RelationshipList.as_view(),
                           name='relationship-list'),
                       url(r'^brands/$', BrandList.as_view(), name='brand-list'),
                       url(r'^about/$', AboutDetail.as_view(),
                           name='about-list'),
                       )
