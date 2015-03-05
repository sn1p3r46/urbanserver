from urbanserver.models import Utente,Evento
from django.contrib.auth.models import User
import datetime

"""
U = User(username="Mario",first_name="Mario")
U.save()
Ut = Utente(user=U,fbID="fbid00",idCell="idCell00")
Ut.save()

U = User(username="Maria",first_name="Maria")
U.save()
Ut = Utente(user=U,fbID="fbid01",idCell="idCell01")
Ut.save()

U = User(username="Mirko",first_name="Mirko")
U.save()
Ut = Utente(user=U,fbID="fbid02",idCell="idCell02")
Ut.save()

U = User(username="Giorgio",first_name="Giorgio")
U.save()
Ut = Utente(user=U,fbID="fbid03",idCell="idCell03")
Ut.save()


E = Evento(titoloSerata = "Friday 27-02-15",artisti="Fab,Fooly",
        data = datetime.date(2015,2,27),
        ora = datetime.time(22,45),
        descr = "Una Serata all'insegna del divertimento e della passione per la buona musica con il \n grandissimo contributo della miglior \n band d'Italia",
        listaBool = 1,
        prevenditeBool = 0,
        prezzoLista = 6,
        prezzoIntero = 8,
        prezzoDopo = 5,
        linkLocandina = "http://linklocandina.com",
        linkFoto = "http://linkallefoto.com",
        linkVideo = "http://linkallefoto.com",
        linkFBEvent = "fbeventfotos.com",
        editTime=datetime.datetime.now())


E.save()


"""
E = Evento(titoloSerata = "saturday 28-02-15",artisti="Fab,Fooly",
        data = datetime.date(2015,2,28),
        ora = datetime.time(22,45),
        descr = "Una Serata all'insegna del divertimento e della passione per la buona musica con il \n grandissimo contributo della miglior \n band d'Italia",
        listaBool = 1,
        prevenditeBool = 0,
        prezzoLista = 6,
        prezzoIntero = 8,
        prezzoDopo = 5,
        linkLocandina = "http://linklocandina.com",
        linkFoto = "http://linkallefoto.com",
        linkVideo = "http://linkallefoto.com",
        linkFBEvent = "fbeventfotos.com",
        editTime=datetime.datetime.now())


E.save()
