from django.contrib.auth.models import User
from urbanserver.models import Evento,Utente


def validateUser(fbID,fbToken):
    try:
        Utente.objects.get(fbID=fbID).user
        print fbToken
        return True

    except:
        return False


#def createUser(fbID,fbToken):
