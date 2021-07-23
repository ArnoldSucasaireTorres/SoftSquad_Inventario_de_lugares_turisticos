from django.shortcuts import render
from .models import Destino
from django.http import JsonResponse

import json

# Lectura del archivo JSON
archivo_json = open('data.json')
data_json = json.load(archivo_json)

# Metodo que filtra los datos de acuerdo al campo: field y el valor de este: field_name
# field: es el campo a filtrar
# name_field: es el nombre del campo a filtrar
def filter_json_data(field, field_name):
    filtered_data = []
    for index in range(len(data_json)):
        if data_json[index][field] != None:
            if field_name in data_json[index][field].lower():
                filtered_data.append(data_json[index])
    return filtered_data

# Metodo que registra los destinos una sola vez
def registrarDestinos():
    if Destino.objects.count() == 0:
        for dest in data_json:
            dest_reg = Destino(
                codigo_destino=dest['codigo'],
                calificacion=0
            )
            dest_reg.save()

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

# Vista de los destinos, se filtran y agregan calificaciones
# request: Solicitud con datos del cliente
def destinationsView(request):
    registrarDestinos()
    if request.method == 'GET':
        datos = destinosCalificados(data_json)
    elif request.method == 'POST':
        calificacion = request.POST['calificacion']
        codigo = request.POST['codigo']
        destino = Destino.objects.get(codigo_destino=codigo)
        #Verificamos si es que el usuario ya califico el sitio
        if len(destino.usuarios.all().filter(id=request.user.id)) != 0:
            print("Ya califico este sitio")
        else:
            destino.calificacion = destino.calificacion + float(calificacion)
            destino.usuarios.add(request.user)
            destino.save()
        datos = destinosCalificados(data_json)
    return render(request, "destinations/all.html", {"destinos": datos})

# Vista para consulta por JSON
# request: Solicitud con datos del cliente
def destinos_json(request):
    filter_field = request.GET.get('filter').lower()
    filter_value = request.GET.get('value').lower()
    data_filtered = filter_json_data(filter_field, filter_value)
    data_filtered = destinosCalificados(data_filtered)
    return JsonResponse(data_filtered, safe=False)

def destinoView(request, id):
    destino = Destino.objects.get(codigo_destino=id)
    return render(request, 'destinations/see.html', {"destino":destino})
    
