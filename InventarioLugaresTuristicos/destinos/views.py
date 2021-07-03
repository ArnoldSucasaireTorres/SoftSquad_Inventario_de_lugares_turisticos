from django.shortcuts import render
import json

archivo_json = open('C:/Users/Michael Secarlos AC/Downloads/data.json')
data_json = json.load(archivo_json)

# Create your views here.
def destinatiosView(request):
    return render(request, "destinations/all.html", {"destinos":data_json})