from django.urls import path
from . import views
from .import jsonQuerys
urlpatterns = [
    path('all', views.destinationsView, name="listDestinations"),

    path('ajaxQuery', jsonQuerys.filtrarDestinos, name='filtered'),
    path('see/<id>/', jsonQuerys.consultarDetino, name="seeDestination"),
    path('calificate/<id>/', jsonQuerys.calificarDestino, name="seeDestination")
]
