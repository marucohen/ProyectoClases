from django.shortcuts import render
from .models import ClaseProducto

# Create your views here.

def pediTuClase(request):

    claseproducto= ClaseProducto.objects.all()

    return render(request, "pediTuClaseApp/pediTuClase.html", {"claseproducto":claseproducto})