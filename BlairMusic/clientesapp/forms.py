from django import forms
from clientesapp.models import Cliente, Orden, Procesos, Articulos, Valores, Imagenes


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ordenForm(forms.ModelForm):
    class Meta:
        model = Orden
        exclude = [
            "fechain",
            "num_orden",
            "client",
            "estado",
        ]


class procesosForm(forms.ModelForm):
    class Meta:
        model = Procesos
        exclude = [
            "reference",
        ]


class articlesForm(forms.ModelForm):
    class Meta:
        model = Articulos
        exclude = [
            "referencia",
        ]


class valoresForm(forms.ModelForm):
    class Meta:
        model = Valores
        exclude = [
            "refer",
            "show_ref",
        ]

class imagenesForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        exclude = [
            "ref_guia",
        ]
