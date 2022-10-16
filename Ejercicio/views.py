from django.shortcuts import render
from Ejercicio.models import Familiar

# Create your views here.
def index(request):
    return render(request, "Ejercicio/Entrega.html")


def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "Ejercicio/familiares.html", 
                {"lista_familiares": lista_familiares})
  
