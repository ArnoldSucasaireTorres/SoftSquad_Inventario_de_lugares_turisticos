from django.shortcuts import render
from .models import Destino
import json

# Lectura del archivo JSON
archivo_json = open('/home/michael/Descargas/data.json')
data_json = json.load(archivo_json)


# Metodo que filtra los datos de acuerdo al campo: field y el valor de este: field_name
# field: es el campo a filtrar
# name_field: es el nombre del campo a filtrar
def filter_json_data(field, field_name):
    filtered_data = []
    for index in range(len(data_json)):
        if data_json[index][field].lower() == field_name:
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
            print("ya califico este sitio")
        else:
            destino.calificacion = destino.calificacion + float(calificacion)
            destino.usuarios.add(request.user)
            destino.save()
        datos = destinosCalificados(data_json)
    return render(request, "destinations/all.html", {"destinos": datos})


# Vista de los destinos filtrados, se agregan calificaciones
# request: Solicitud con datos del cliente
def destinationsFilteredView(request):
    if request.method == 'GET':
        filter_field = request.GET.get('filter')
        filter_value = request.GET.get('value')
        data_filtered = filter_json_data(filter_field.lower(), filter_value.lower())
        data_filtered = destinosCalificados(data_filtered)
        return render(request, "destinations/filtered.html", {"destinos": data_filtered})
    else:
        data = destinosCalificados(data_json)
        return render(request, "destinations/all.html", {"destinos": data})
