from django.shortcuts import render
from .models import Destino
import json

# Lectura del archivo JSON
archivo_json = open('data.json')
data_json = json.load(archivo_json)

# Metodo que registra los destinos una sola vez
def registrarDestinos():
    if Destino.objects.count() == 0:
        for dest in data_json:
            dest_reg = Destino(
                codigo_destino=dest['codigo'],
                calificacion=0
            )
            dest_reg.save()

# Metodo que filtra los datos de acuerdo al campo: field y el valor de este: field_name
# field: es el campo a filtrar
# name_field: es el nombre del campo a filtrar
def filter_json_data(field, field_name):
    filtered_data = []
    for index in range(len(data_json)):
        if data_json[index][field] != None:
            if field_name in str(data_json[index][field]).lower():
                filtered_data.append(data_json[index])
    return filtered_data

# Metodo que agrega el campo calificacion al arreglo de destinos
# data: destinos a los que filtrar
def destinosCalificados(data):
    calificated_data = data
    for dest in calificated_data:
        dest_data = Destino.objects.get(codigo_destino=dest['codigo'])
        if len(dest_data.usuarios.all())!=0:
            dest["calificacion"] = dest_data.calificacion/len(dest_data.usuarios.all())
        else:
            dest["calificacion"] = 0
    return calificated_data

#_________________________________Vistas_________________________________#


# Vista de los destinos, se filtran y agregan calificaciones
# request: Solicitud con datos del cliente
def destinationsView(request):
    registrarDestinos()
    datos = destinosCalificados(data_json)
    return render(request, "destinations/all.html", {"destinos": datos})
