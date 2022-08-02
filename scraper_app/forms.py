from django import forms
from .models import Indice

class AddIndiceForm(forms.ModelForm):
    class Meta:
        model = Indice
        fields = ('name',)