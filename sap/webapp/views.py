from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from personas.models import Persona


# Create your views here.
def bienvenida(request):
    pagina = loader.get_template('saludo.html')
    return HttpResponse(pagina.render())
def hola(request, nombre):
    apellido = request.GET['apellido']
    nivel = request.GET['nivel']
    curso = request.GET['curso']
    pagina = loader.get_template('saludo.html')
    nombreCompleto = nombre + " " + apellido
    datos = {'nombre': nombreCompleto , 'curso':curso, 'nivel':nivel}
    return HttpResponse(pagina.render(datos, request))

def edad(request, edad):
    pagina = loader.get_template('edad.html')
    mensaje = {'edad': edad}
    return HttpResponse(pagina.render(mensaje, request))

def mostrar_personas (request):
    cantidad_personas = Persona.objects.count()
    personas = Persona.objects.all().values()

    nombres_personas = list()
    for persona in personas:
        nombres_personas.append(persona['nombre'])

    datos =  {'cantidad': cantidad_personas, 'personas': personas,  'nombres_personas':  nombres_personas}
    pagina = loader.get_template('personas.html')
    return HttpResponse(pagina.render(datos, request))


