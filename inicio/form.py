from django import forms


class FormularioCrearEquipo(forms.Form):
    
    procesador = forms.CharField(max_length=20)
    ram = forms.CharField(max_length=20)
    mother = forms.CharField(max_length=20)
    video = forms.CharField(max_length=20)
    gabinete = forms.CharField(max_length=20)
    imagen = forms.ImageField(required=False)
    