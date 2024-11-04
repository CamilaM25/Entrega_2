from django import forms
from .models import Equipo,Responsable

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'