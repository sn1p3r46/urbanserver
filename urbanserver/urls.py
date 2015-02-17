from django.conf.urls import patterns, url
from urbanserver import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about' ),
        url(r'^createvent/', views.createEvent, name='Event_creation'),
        url(r'^getevents', views.getEvents, name='Get_Events'),
        )
