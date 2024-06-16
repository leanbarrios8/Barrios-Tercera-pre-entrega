from django import forms
from .models import Moneda

class CrearMoneda(forms.ModelForm):
    class Meta:
        model = Moneda
        fields = ['nombre', 'valor']