from django.urls import path

from ProyectoClasesApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name= "Home"),
    path('servicios',views.servicios, name= "Nosotros"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)