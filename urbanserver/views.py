from django.shortcuts import render
from django.http import HttpResponse
from forms.eventForm import EventoModelForm
from urbanserver.models import Evento,Utente
from django.contrib.auth.models import User
from django.core import serializers
from urbanserver.facebook import validateUser, getFacebookName
import random
import string


import json
import datetime



# Create your views here.



def index(request):
    context_dict = {'boldmessage': "Amaro Montevero.. Sapore Negro"}
    return render(request, 'urbanserver/index.html', context_dict)

def about(request):
    return render(request, 'urbanserver/about.html')

def createEvent(request):
    if request.method == 'GET':
        form = EventoModelForm()
    else:
        # A POST request: Handle Form Upload
        form = EventoModelForm(request.POST) # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            form.save()
            return render(request, 'urbanserver/addEvent.html', {'form': form})
    return render(request, 'urbanserver/addEvent.html', {'form': form})


def getEvents(request):
    d = Evento.objects.all()
    data = serializers.serialize('json', d, indent=2)
    #data = json.dumps(json.loads(data), indent=4)
    return HttpResponse(data, content_type="application/json")


def getNextEvent(request):
    day = request.GET.get('day',6)
    today = datetime.datetime.now().date() + datetime.timedelta(days=1)
    e = Evento.objects.filter(data__week_day=day, data__gte=today).order_by("data")[:1]
    data = serializers.serialize('json', e, indent=2)
    #data = json.dumps(json.loads(data), indent=4)
    return HttpResponse(data, content_type="application/json")


def getUsersInLista(request):
    eventID = request.GET.get('event',0)
    E = Evento.objects.get(pk=eventID)
    Lista = []
    for i in E.userInLista.all():
        c = {'nome': i.first_name, 'cognome':i.last_name}
        c = (i.first_name, i.last_name)
        Lista.append(c)
    data = json.dumps(Lista,indent=2)
    return HttpResponse(data, content_type="application/json")


def newUser(request):
    fbID = request.GET.get('fbID',False)
    fbToken = request.GET.get('fbToken',False)
    idCell = request.GET.get('idCell',False)

    if not (fbID and  fbToken and idCell):
        return HttpResponse("No GET arguments passed or passed Wrong")

    if validateUser(fbID,fbToken):
        nome, cognome = getFacebookName(fbID)
        username = ''.join(random.SystemRandom().choice(string.uppercase + string.digits) for _ in xrange(29))

        try:
            user = Utente.objects.get(fbID = fbID)
            user.idCell = idCell
            user.save()
            return HttpResponse("OK")

        except Utente.DoesNotExist:
            nome, cognome = getFacebookName(fbID)
            U = User(username = username, first_name = nome, last_name = cognome)
            U.save()
            Ut = Utente(user = U,fbID = fbID, idCell = idCell)
            Ut.save()
            return HttpResponse("OK")
    else:
        return HttpResponse("ValidateUser Function FAILED")


def putUserINLista(request):
    fbID = request.GET.get('fbID',False)
    fbToken = request.GET.get('fbToken',False)
    eventID = request.GET.get('event',False)

    if not (fbID and  fbToken and eventID):
        return HttpResponse("No GET arguments passed or passed Wrong")
    try:
        if validateUser(fbID,fbToken):
            eventID = request.GET.get('event',1)
            E = Evento.objects.get(pk=eventID)
            E.userInLista.add(Utente.objects.get(fbID=fbID).user)
            return HttpResponse("OK")
        else:
            return HttpResponse("ValidateUser Function FAILED")
    except:
        return HttpResponse("Something Wrong.. Maybe The user is not in the DB or the event PK is Wrong")



def getModificationDate(request):
    day = request.GET.get('day',6)
    today = datetime.datetime.now().date() + datetime.timedelta(days=1)
    e = Evento.objects.filter(data__week_day=day, data__gte=today).order_by("data")[:1]
    if e.count()==0:
        return HttpResponse("empty")
    e = e[0]
    editDate = e.editTime.isoformat()
    pk = e.pk
    data = [editDate,pk]
    data = json.dumps(data,indent=2)
    return HttpResponse(data, content_type="application/json")
