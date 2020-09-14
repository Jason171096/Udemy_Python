from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
    
"""
lenguajes = ['C#', "C", "Python"]

def index_i(requets):
    return render(requets, 'index.html', {
        "mivar": "Soy un dato",
        "lenguajes": lenguajes
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def contacto(request, nombre):
    return HttpResponse(layout+f"Mi contacto {nombre}")