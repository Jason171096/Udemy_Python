from django.shortcuts import HttpResponse, redirect, render
from miapp.models import Article, Category
from miapp.forms import FormArticle
from django.contrib import messages

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

def crear_articulo(request):
    articulo = Article(
        title = 'Champiñones',
        content = 'EDF',
        public = True,
    )

    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title}")

def articulo(request):
    articulo = Article.objects.get(id=1)
    return HttpResponse(f"Articulo: {articulo.title}")

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Papas"
    articulo.content = "Libro de Papas"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.title}")

def articulos(request):

    articulo = Article.objects.all()

    #articulo = Article.objects.filter(title = 'articulo').exclude(public=True)

    return render(request, 'articulos.html', {
        'articulos': articulo
    })

def eliminar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')

def create_article(request):
    return render(request, 'create_article.html')

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse("Articulo creado")
    
    else:
        return HttpResponse("<h2>No se recibieron los datos</h2>")


def create_forms_article(request):

    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            #Crear mensaje flash solo se muestra una vez 
            messages.success(request, f"Has creado correctamente el articulo {articulo.id}")

            return redirect('articulos')
    
    else:
        formulario = FormArticle()

    return render(request, 'create_forms_article.html',{
            'form': formulario
        })