from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'nationality']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration_seconds', 'genre', 'artist']
        widgets = {
            'duration_seconds': forms.NumberInput(attrs={'min': 0}),
        }
