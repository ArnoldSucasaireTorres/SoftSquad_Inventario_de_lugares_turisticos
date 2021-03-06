from .models import Destino
from django.http import JsonResponse
from . import views
import json

# Funcion para calificar/recibir por JSON
# request: Solicitud con datos del cliente
def calificarDestino(request, id):
    if request.user.is_authenticated:
        destino = Destino.objects.get(codigo_destino=id)
        #Verificamos si es que el usuario ya califico el sitio
        if len(destino.usuarios.all().filter(id=request.user.id)) != 0:
            print("Ya califico este sitio")
        else:
            calificacion = request.POST['calificacion']
            for key, value in request.POST.items():
                print('Key: ', key) 
                print('Value: ', value)
            print("\n\n")
            destino.calificacion = destino.calificacion + float(calificacion)
            destino.usuarios.add(request.user)
            destino.save()
    else:
        print("No esta authenticado")
    return consultarDetino(request, id)

# Funcion para consulta por JSON
# request: Solicitud con datos del cliente
def filtrarDestinos(request):
    filter_field = request.GET.get('filter').lower()
    filter_value = request.GET.get('value').lower()
    data_filtered = views.filter_json_data(filter_field, filter_value)
    data_filtered = views.destinosCalificados(data_filtered)
    return JsonResponse(data_filtered, safe=False)

# Funcion para consular el destino por JSON
# request: Solicitud de datos del cliente
def consultarDetino(request, id):
    destino = views.filter_json_data('codigo', id)
    destino = views.destinosCalificados(destino)
    return JsonResponse(destino[0] , safe=False)
    
# Funcion para consultar los restaurantes por JSON
# request: Solicitud de datos del cliente
def consultarRestaurantes(request, id):
    # Lectura del archivo de restaurantes
    archivo_json = open('restaurantes.json')
    data_json = json.load(archivo_json)

    provincia = ""
    #Busqueda de la provincia del destino
    for destino in views.data_json:
        if str(destino['codigo']) == str(id):
            provincia = destino['provincia'].lower()

    #Busqueda de los restaurantes del destino
    restaurantes = []
    for rest in data_json:
        if rest['provincia'] == provincia:
            restaurantes.append(rest)
    return JsonResponse(restaurantes, safe=False)

