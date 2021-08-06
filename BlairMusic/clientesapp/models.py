from django.db import models
from datetime import datetime, date
from django.forms import ModelForm, Textarea


# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=100, default='direccion')


class Orden(models.Model):
    STATUS = [
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
    ]
    num_orden = models.CharField(max_length=20, default='')
    fechain = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    fechaout = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    instrumento = models.CharField(max_length=30, default='')
    marca = models.CharField(max_length=20)
    referencia = models.CharField(max_length=30, default='')
    serial = models.CharField(max_length=15, default='')
    encargado = models.CharField(max_length=50, default='')
    abono = models.CharField(max_length=15, default='')
    # procesos = models.TextField(default='')
    estado = models.CharField(max_length=50, null=True, choices=STATUS, default='En proceso')
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE, default='', related_name="client")
    # Cuerdas
    cuerdas = models.CharField(max_length=50, default='')
    cero8 = models.BooleanField(default=False)
    cero9 = models.BooleanField(default=False)
    cero10 = models.BooleanField(default=False)
    cero11 = models.BooleanField(default=False)
    cero12 = models.BooleanField(default=False)
    lastrajo = models.BooleanField(default=False)
    afinacion = models.CharField(max_length=50, default='')
    # Clase de Instrumento
    pfijo = models.BooleanField(default=False)
    pflotante = models.BooleanField(default=False)
    elac = models.BooleanField(default=False)
    acustica = models.BooleanField(default=False)
    bajo = models.BooleanField(default=False)
    teclado = models.BooleanField(default=False)
    vientos = models.BooleanField(default=False)
    percusion = models.BooleanField(default=False)
    pedal = models.BooleanField(default=False)
    amplificador = models.BooleanField(default=False)
    otro = models.CharField(max_length=50, default='', null=True)
    # Estuche
    negativo = models.BooleanField(default=False)
    afirmativo = models.BooleanField(default=False)
    lona = models.BooleanField(default=False)
    semi = models.BooleanField(default=False)
    duro = models.BooleanField(default=False)
    caja = models.BooleanField(default=False)


class Procesos(models.Model):
    process = models.TextField()
    reference = models.ForeignKey(Orden, on_delete=models.CASCADE, default='', related_name="reference")


class Articulos(models.Model):
    articulo = models.CharField(max_length=50, default='')
    orden_ref = models.ForeignKey(Orden, on_delete=models.CASCADE, default='', related_name="orden_ref")


class Valores(models.Model):
    costo = models.IntegerField(max_length=20, default='')
    refer = models.ForeignKey(Orden, on_delete=models.CASCADE, default='', related_name="refer")
