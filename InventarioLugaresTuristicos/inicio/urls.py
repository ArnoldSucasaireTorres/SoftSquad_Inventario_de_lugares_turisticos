from django.urls import path
from . import views

urlpatterns = [
    path('', views.myHomeView , name="index"),
]



