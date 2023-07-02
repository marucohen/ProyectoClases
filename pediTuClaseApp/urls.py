from django.urls import path

from . import views


urlpatterns = [
    path('',views.pediTuClase, name="Pedi tu clase")
]

