from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'description', 'adopted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
