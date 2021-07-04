from django.shortcuts import render
from .models import Destino
import json

# A continuacion se hace la lectura del archivo JSON
archivo_json = open('C:/Users/Michael Secarlos AC/Downloads/data.json')
data_json = json.load(archivo_json)


# Ahora se definen los metodos de filtrado
# field: es el campo a filtrar
# name_field: es el nombre del campo a filtrar
def filter_json_data(field, field_name):
    filtered_data = []
    for index in range(len(data_json)):
        if data_json[index][field].lower() == field_name:
            filtered_data.append(data_json[index])
    return filtered_data


#
def registrarDestinos():
    if Destino.objects.count() == 0:
        for dest in data_json:
            dest_reg = Destino(
                codigo_destino=dest['codigo'],
                calification=0
            )
            dest_reg.save()

# Create your views here.
def destinationsView(request):
    registrarDestinos()
    if request.method == 'GET':
        return render(request, "destinations/all.html", {"destinos": data_json})
    elif request.method == 'POST':
        #if request.user.is_authenticated():
        #    codigo = request.POST['codigo']
        #    calificacion = request.POST['calificacion']
        #    registro_destino = Destino(
        #        codigo=codigo,
        #        calificacion=calificacion,
        #        users=request.user
        #    )
        #    registro_destino.save()
        return render(request, "destinations/all.html", {"destinos": data_json})


def destinationsFilteredView(request):
    if request.method == 'GET':
        filter_field = request.GET.get('filter')
        filter_value = request.GET.get('value')
        data_filtered = filter_json_data(filter_field.lower(), filter_value.lower())
        return render(request, "destinations/filtered.html", {"destinos": data_filtered})
    else:
        return render(request, "destinations/all.html", {"destinos": data_json})
