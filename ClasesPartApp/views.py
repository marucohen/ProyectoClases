from django.shortcuts import render
from ClasesPartApp.models import ClasesPart

# Create your views here.

def clases(request):
    
    clasesParticulares=ClasesPart.objects.all()
    return render(request, "ClasesPartApp/clases.html", {"clasesParticulares": clasesParticulares})