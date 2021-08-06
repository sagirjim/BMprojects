from django import forms
from clientesapp.models import Cliente, Orden, Procesos, Articulos, Valores


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ordenForm(forms.ModelForm):
    class Meta:
        model = Orden
        exclude = [
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
        model = Articulos
        exclude = [
            "refer",
        ]
