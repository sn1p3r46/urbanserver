from django.shortcuts import render
from django.http import HttpResponse
from forms.eventForm import EventoModelForm
from urbanserver.models import Evento
from django.core import serializers

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
