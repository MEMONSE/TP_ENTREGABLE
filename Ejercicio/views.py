from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Ejercicio/Entrega.html")


def mostrar_familiares(request):
  lista_familiares = ["Mama","pe"] #Familiar.objects.all()
  return render(request, "Ejercicio/Entrega.html", 
                {"lista_familiares": lista_familiares})