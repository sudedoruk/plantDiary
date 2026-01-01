from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            'name', 
            'species', 
            'photo', 
            'location', 
            'irrigation_frequency'
        ]