from django.urls import re_path
from django.urls import path

from . import views


urlpatterns = [
    re_path('^addprojects/$', views.addProjects, name = 'addprojects'),
    re_path('^addevents/$', views.addEvents, name = 'addevents'),
    re_path('^$', views.index, name='index'),
    re_path('^aboutus/$', views.aboutus, name='aboutus'),
    re_path('^blog/$', views.blog, name='blog'),
    re_path('^events/$', views.events, name='events'),
    re_path('^projects/$', views.projects, name='projects'),
    # path('logout/', views.logout, name='logout'),
    re_path('^eventdescription/<int:pk>$', views.event_template, name='event_template'),
    path("projects/<slug:ProjectID>", views.project_detail, name="project_detail"),
    path("events/<slug:EventID>", views.event_detail, name="event_detail")
]
