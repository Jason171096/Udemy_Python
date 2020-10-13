"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from miapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_i, name= "index_i"),
    path('inicio/', views.index_i, name= "index"),
    path('hola_mundo/', views.hola_mundo, name="hola_mundo"),
    path('contacto/<str:nombre>', views.contacto, name= "contacto"),
    path('crear_articulo/', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar_articulo/<int:id>', views.editar_articulo),
    path('articulos/', views.articulos, name="articulos"),
    path('eliminar_articulo/<int:id>', views.eliminar_articulo, name="borrar"),
    path('create_article/', views.create_article, name="create_article"),
    path('save_article/', views.save_article, name="save_article"),
    path('create_forms_article/', views.create_forms_article, name="create_forms_article")
]
