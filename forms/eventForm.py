from urbanserver.models import Evento
from django.forms import ModelForm

class EventoModelForm(ModelForm):
    class Meta:
        model = Evento
        exclude = ['userInLista']
