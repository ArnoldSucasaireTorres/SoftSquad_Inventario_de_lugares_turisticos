from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHomeView(request, *args, **kwargs):
    f = open("provinciasAQP.json",encoding="utf8")
    provincias=f.read()
    f.close()
    f = open("distritosAQP.json",encoding="utf8")
    distritos=f.read()
    f.close()
    f = open("data.json", encoding="utf8")
    turisticos=f.read()
    f.close()
    return render(request,'maps/index.html',{'provincias':provincias,'distritos':distritos,'turisticos':turisticos})
