from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Venta_garage

# Create your views here.
def room(request):

	return render(request, 'project_begins/room.html')

def room_stuff(request):

	return render(request, 'project_begins/cosas.html',{})


def home_view(request):

	return render(request, 'project_begins/home.html',{})

def fecha_actual(request):
	ahora = datetime.datetime.now()
	la_tarde = ahora.hour > 12   						
	lista_cosas = Venta_garage.objects.all()
	almuerzo = ahora.hour > 12
	nombre = 'hans'
	return render(request, 'project_begins/fechactual.html', {'hora': ahora, 'x': nombre, 'tarde':la_tarde, 'listfood':almuerzo, 'lista':lista_cosas})
