from django.conf.urls import patterns, url
from urbanserver import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about' ),
        url(r'^createvent/', views.createEvent, name='Event Creation'),
        url(r'^getevents', views.getEvents, name='Get All Events'),
        url(r'^getnextevent/$', views.getNextEvent, name='Get Next Event'),
        url(r'^getusersinlista/$', views.getUsersInLista, name='Get Users In Lista'),
        url(r'^putuserinlista/$', views.putUserINLista, name='Put User In Lista'),
        url(r'^getmodificationdate/$', views.getModificationDate, name='get modification date'),
        url(r'^newuser/$', views.newUser, name='new user')
        )
