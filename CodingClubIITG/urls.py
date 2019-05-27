from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('blog/', views.blog, name = 'blog'),
    path('events/', views.events, name = 'events'),
    path('projects/', views.projects, name = 'projects'),
]