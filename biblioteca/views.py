from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from biblioteca.form import LibroForm
from django.shortcuts import redirect, render
from biblioteca.models import Libro
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
#from django.core.urlresolvers import reverse

# Create your views here.


def Home(request):
    return render(request, 'Home.html')


def buscar(request):
    errors = []
    if'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q)>20 :
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request,'resultados.html',{'libros':libros,'query':q})
    
    return render(request, 'formulario_buscar.html', {'errors': errors})

def registrar_libro(request):
    if request.method =='POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(lista_libros)
    else:
        form = LibroForm()
    return render(request, 'registro_libro.html', {'form':form})

def lista_libros(request):
    libros = Libro.objects.all().order_by('id')
    return render(request, 'lista_libros_def.html', {'Libros':libros})

def actualizar_libro(request, id_libro):
    libro = Libro.objects.get(id= id_libro)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect(lista_libros)
    return render(request, 'registro_libro.html', {'form':form})

def eliminar_libro(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == 'POST':
        libro.delete()
        return redirect(lista_libros)
    return render(request, 'eliminar_libro.html', {'Libros':libro})



class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'registro_libro.html'
    #success_url = redirect('Home')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'registro_libro.html'
    #success_url = redirect('Home')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'eliminar_libro_def.html'
    #success_url = redirect('Home')

class LibroList(ListView):
     model = Libro
     template_name = 'lista_libros.html'
    
class HomeView(TemplateView):
    template_name = 'Home.html'



class LibroDetail(DetailView):
    model = Libro
