from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    context_dict = {'boldmessage': "Amaro Montevero.. Sapore Negro"}
    return render(request, 'urbanserver/index.html', context_dict)

def about(request):
    return render(request, 'urbanserver/about.html')
