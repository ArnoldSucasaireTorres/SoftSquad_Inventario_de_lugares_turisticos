from django.urls import path
from . import views

urlpatterns = [
    path('all', views.destinationsView, name="listDestinations"),
    path('ajaxQuery', views.destinos_json, name='filtered'),
    path('see/<id>/', views.destinoView, name="seeDestination")
]
