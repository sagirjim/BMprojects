# Generated by Django 3.1.7 on 2021-06-26 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientesapp', '0002_auto_20210624_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('En proceso', 'En proceso'), ('Entregado', 'Entregado')], max_length=50, null=True),
        ),
    ]