import json
import urllib2
from urllib2 import HTTPError
###
from django.contrib.auth.models import User
from urbanserver.models import Evento,Utente


APPID     = "727751257343149"
APPSECRET = "b079603138ffe5beee21cd62f9f3c78d"
APPTOKEN  = "727751257343149|9LFJJ1nEq1QGSjTgBopWY94vheQ"


def validateUser(fbID,fbToken):
    try:
        data = json.load(urllib2.urlopen('https://graph.facebook.com/debug_token?input_token=' + fbToken + '&access_token=' + APPTOKEN))['data']
        if (data['is_valid'] == True and data['app_id'] == APPID and data['user_id'] == fbID):
            print data
            return True
        else:
            return False
    except:
        return False

def validateUser1(fbID,fbToken):
    try:
        data = json.load(urllib2.urlopen('https://graph.facebook.com/debug_token?input_token=' + fbToken + '&access_token=' + APPID +'|'+APPSECRET))['data']
        if (data['is_valid'] == True and data['app_id'] == APPID and data['user_id'] == fbID):
            return True
        else:
            return False
    except:
        return False



def getFacebookName(idFacebook):
    try:
        if isinstance(idFacebook, unicode) or isinstance(idFacebook, str):
            print 'getFacebookName: is string ' + idFacebook
            print 'https://graph.facebook.com/' + idFacebook+'&access_token=' + APPTOKEN
            ris = json.load(urllib2.urlopen('https://graph.facebook.com/' + idFacebook+'?access_token=' + APPTOKEN))
            print 'risposta facebok: ' + str(ris)
            return ris['first_name'],ris['last_name']

        else:
            print 'parametro errato'
            return None

    except HTTPError, e:
        print 'Could not download page ' + str(e)
    except Exception, e:
        print 'Error getFacebookName: ' + str(e)
