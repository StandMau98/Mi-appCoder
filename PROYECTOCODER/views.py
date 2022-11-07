from datetime import datetime
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Template, Context #loader
from django.template import loader



def vista_saludo(request):
    return HttpResponse("<h1>Hola Django</h1>")

def dia_hoy(request, nombre):
    hoy = datetime.now()
    
    respuesta = f"hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)

def nacimiento(request , edad):
   anio_nacimiento = int(edad) - datetime.now().year

   respuesta = f"<h1> Tu año de nacimiento fue en {anio_nacimiento}</h1>"
   return HttpResponse(respuesta)

def vista_plantilla(request):
    #abrimos archivo
    archivo = open(r"\Users\mauro\Documents\DJango_TP\codigo\PROYECTOCODER\template\Plantilla_buena.html")
    
    
    #creamos objeto plantilla
    plantilla = Template(archivo.read())
    
    #cerramos archivo para liberar recursos
    archivo.close()

    #creamos diccionario
    listado_alumnos = ["Mauro Romero","Camila Cuenca", "Diego Ibarra", "Barbara Vivante"]
    datos = {"tecnologia": "Python", "listado_alumnos": [listado_alumnos], "fecha": datetime.now()}
    
    #creamos contexto
    contexto = Context(datos)
     
    #renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    #retornamos la respuesta
    return HttpResponse(documento)


def vista_alumnos(request):
    #abrimos archivo
    archivo = open(r"\Users\mauro\Documents\DJango_TP\codigo\PROYECTOCODER\template\listado_alumno.html")
    
    #creamos el template
    plantilla = Template(archivo.read())
    
    #cerramos archivo, para liberar recursos
    archivo.close()

    #creamos diccionario
    listado_alumnos = ["Mauro Romero","Camila Cuenca", "Diego Ibarra", "Barbara Vivante"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

   
def vista_alumnos2(request):
    #creamos el diccionario de datos
    listado_alumnos = ["Mauro Romero","Camila Cuenca", "Diego Ibarra", "Barbara Vivante"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    
    plantilla = loader.get_template("listado_alumno.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)
    