from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='descripcion')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Fecha creado')

    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='articles')
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='Categorias', null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True, verbose_name='Fecha creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Fecha editado')

    class Meta():
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.title