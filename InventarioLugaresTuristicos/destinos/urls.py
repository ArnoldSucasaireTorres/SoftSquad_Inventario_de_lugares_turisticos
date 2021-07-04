from django.urls import path
from . import views

urlpatterns = [
    path('all', views.destinationsView, name="listDestinations"),
    path('filtered', views.destinationsFilteredView, name="listFilteredDestinations"),
]



