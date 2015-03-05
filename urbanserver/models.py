from django.db import models
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import datetime



# Create your models here.

class Utente(models.Model):
    user = models.OneToOneField(User, unique=True)
    fbID = models.CharField(max_length=500,default="FACEBOOK UID", unique=True)
    idCell = models.CharField(max_length=500,default="CELL UID", unique=True)
    linkFoto = models.CharField(max_length=200, default="link foto Utente")
    #compleanno = models.DateField(default=None,blank=True, null=True)
    presenze = models.IntegerField(default="0")


    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user.first_name

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
    editTime = models.DateTimeField(default = datetime.datetime.now())
    linkFoto = models.ImageField(upload_to="static/images/", blank=True, null=True)
    ueID = models.IntegerField(default=0)

    def save(self):
        self.ueID +=1
        super(Evento, self).save()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.titoloSerata

"""
class Devices(models.Model):
    user = models.ForeignKey(User)
    device = models.CharField(max_length=500)

    def __unicode__(self):
        return self.user.first_name
"""
