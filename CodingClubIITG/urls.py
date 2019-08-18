from django.urls import re_path

from . import views


urlpatterns = [
    re_path('^addprojects/$', views.addProjects, name = 'addprojects'),
    re_path('^$', views.index, name='index'),
    re_path('^aboutus/$', views.aboutus, name='aboutus'),
    re_path('^blog/$', views.blog, name='blog'),
    re_path('^events/$', views.events, name='events'),
    re_path('^projects/$', views.projects, name='projects'),
    re_path('^eventdescription/<int:pk>$', views.event_template, name='event_template')
]
