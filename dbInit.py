from urbanserver.models import Utente,Evento
from django.contrib.auth.models import User
import datetime


U = User(username="Marione")
U.save()
Ut = Utente(user = U,fbID="fbid00")
Ut.save()

U = User(username="Alex")
U.save()
Ut = Utente(user = U,fbID="fbid01")
Ut.save()

U = User(username="SvenVatt")
U.save()
Ut = Utente(user = U,fbID="fbid02")
Ut.save()


U = User(username="Maria")
U.save()
Ut = Utente(user = U,fbID="fbid03")
Ut.save()

E = Evento(
    titoloSerata = "Friday 27-02-15"
    artisti = "Fab,Fooly"
    data = datetime.date(2015,2,27)
    ora = datetime.time(22:35)
    descr = "Descizione Evento"
    listaBool = 1
    prevenditeBool = 0
    prezzoLista = 6
    prezzoIntero = 8
    prezzoDopo = 5
    linkLocandina = "linkLocandina"
    linkFoto = "http://foto.foto.com"
    linkVideo = "linkVideo"
    linkFBEvent = "linkFb"
    editTime = models.DateTimeField(default = datetime.now())
)
