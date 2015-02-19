from django.db import models
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Utente(models.Model):
    user = models.OneToOneField(User, unique=True)
    fbID = models.CharField(max_length=500,default="FACEBOOK UID", unique=True)
    linkFoto = models.CharField(max_length=200, default="link foto Utente")
    compleanno = models.DateField(default=None,blank=True)
    presenze = models.IntegerField(default="0")


class Evento(models.Model):
    titoloSerata = models.CharField(max_length=200, default ="TitoloSerata")
    artisti = models.CharField(max_length=300, default="Nomi Artisti")
    data = models.DateField("Data Evento", unique=True)
    ora = models.TimeField("Ora Evento")
    descr = models.TextField(default="Descrizione Evento")
    listaBool = models.IntegerField(default="0")
    userInLista = models.ManyToManyField(User, blank=True, serialize=False)
    prevenditeBool = models.IntegerField(default="0")
    prezzoLista = models.IntegerField(default="0")
    prezzoIntero = models.IntegerField(default="0")
    prezzoDopo = models.IntegerField(default="0")
    linkLocandina = models.CharField(max_length=500, default ="LinkLocandina")
    linkFoto = models.CharField(max_length=500, default ="LinkFoto")
    linkVideo = models.CharField(max_length=500, default ="LinkVideo")
    linkFBEvent = models.CharField(max_length=500, default ="LinkFBEvent")


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titoloSerata
