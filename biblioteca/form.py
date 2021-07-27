from biblioteca.models import Libro
from django import forms




class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada',
        ]

        labels = {
            'titulo': 'Titulo',
            'autores': 'Autores',
            'editor': 'Editor',
            'fecha_publicacion': 'Fecha de publicacion',
            'portada': 'Portada',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'editor': forms.Select(),
        }
