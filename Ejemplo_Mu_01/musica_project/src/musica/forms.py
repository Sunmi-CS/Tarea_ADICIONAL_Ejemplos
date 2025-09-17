from django import forms
from .models import Artista, Musica

class ArtistaFormulario(forms.ModelForm):
    class Meta:
        model = Artista
        campo = ['nombre','nacionalidad']

class CancionFormulario(forms.ModelForm):
    class Meta:
        model = Musica
        campo = ['titulo','duracion','genero','artista']
        complemento = {
            'duracion':forms.NumberInput(attrs={'min': 0}),
        }