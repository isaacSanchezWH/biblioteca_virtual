from django.db import models
# Create your models here.

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=40)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self) :
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos= models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def  __unicode__(self) :
         return '{} {}'.format(self.nombre,self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas',null=True)


    def  __unicode__(self) :
        return self.titulo