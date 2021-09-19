from django.shortcuts import render
from django.http import HttpResponse

def suma(request,var1,var2):
    respuesta=var1+var2 
    return HttpResponse("La  suma de  " + str(var1) + " y " +  str(var2) + " es "  + str(respuesta))
def resta(request,var1,var2):
    respuesta=var1-var2
    return HttpResponse("La  resta de  " + str(var1) + " y " +  str(var2) + " e s"  + str(respuesta))
def multiplicacion(request,var1,var2):
    respuesta=var1*var2
    return HttpResponse("La  multiplicacion de " + str(var1) + " y " +  str(var2) + " es "  + str(respuesta))
def division(request,var1,var2):
    respuesta=var1/var2
    return HttpResponse("La  division de " + str(var1) + " y " +  str(var2) + " es "  + str(respuesta))


# Create your views here.
