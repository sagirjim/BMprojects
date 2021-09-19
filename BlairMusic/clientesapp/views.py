from django.shortcuts import render, redirect, get_object_or_404
from .forms import clienteForm, ordenForm, procesosForm, articlesForm, valoresForm, imagenesForm
from .models import Cliente, Orden, Procesos, Articulos, Valores, Imagenes
from .filters import ClienteFilter
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def home(request):
    return render(request, 'home.html', {})


# Herramienta de busqueda para encontrar Clientes
def clientesindex(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if nombre == item.nombre:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese Nombre")

    if 'cedula' in request.GET:
        cedula = request.GET['cedula']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if cedula == item.cedula:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese numero de Cedula")

    return render(request, "clientesindex.html", {})


# Herramienta de Busqueda para asignar un cliente a una orden.
def orderforclient(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if nombre == item.nombre:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese Nombre")
    if 'cedula' in request.GET:
        cedula = request.GET['cedula']
        cliente = Cliente.objects.all()
        for item in cliente:
            indice = item.id
            if cedula == item.cedula:
                return redirect("clientepag", id=indice)
            else:
                messages.error(request, "No se encontro cliente con ese numero de Cedula")

    return render(request, "orderforclient.html", {})


# Funcion para guardar el formulario de un cliente nuevo
def clnt(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            init = form.save()

            return redirect("clientepag", id=init.id)

    else:
        form = clienteForm()
    return render(request, 'index.html', {'form': form})


def view(request):
    cliente = Cliente.objects.all()
    return render(request, "view.html", {'cliente': cliente})


def delete(request, id):
    otro = Cliente.objects.filter(id=id)
    otro.delete()
    return redirect('/view')


# Funcion para editar los datos de un cliente
def edit(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "edit.html", {'cliente': cliente})


# Funcion para guardar las modificaciones a los datos de un cliente
def update(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'GET':
        form = clienteForm(instance=cliente)
        return redirect("clientepag", id=id)

    else:
        form = clienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect("clientepag", id=id)
        else:
            form = clienteForm()
            return redirect("clientepag", id=id)


# Visualizacion de los datos del cliente
def clientepag(request, id):
    cliente = Cliente.objects.get(id=id)
    ordenes = Orden.objects.all()
    context = {
        'cliente': cliente,
        'ordenes': ordenes,
    }
    return render(request, 'clientepag.html', context)


# Herramienta para busqueda de una orden especifica
def ordenindex(request):
    if 'orden' in request.GET:
        orden = request.GET['orden']
        ordenes = Orden.objects.all()
        for item in ordenes:
            indice = item.id
            if orden == item.num_orden:
                return redirect("ordenview", id=indice)
            else:
                messages.error(request, "No se encontro una Orden con ese numero")
    if 'cliente' in request.GET:
        cliente = request.GET['cliente']
        ordenes = Orden.objects.all()
        for item in ordenes:
            indice = item.id
            if cliente == item.client.nombre:
                print(item.client)
                return redirect("ordenview", id=indice)
            else:
                messages.error(request, "No se encontro una Orden asociada a ese Nombre")

    return render(request, "ordenindex.html", {})


# Formulario para una orden nueva
def ordenfill(request, client_id):
    fecha = datetime
    if request.method == 'POST':
        orden = ordenForm(request.POST, initial={'num_orden': '1'})
        #orden = ordenForm(request.POST)
        #initial = 0
        last = Orden.objects.all().last()
        if orden.is_valid():
            if last is None:
                new_num = 0
            else:
                new_num = int(last.num_orden) + 1
            norden = str(new_num).zfill(4)
            orden.instance.num_orden = (norden)
            orden.instance.client_id = client_id
            orden.instance.estado = request.POST.get("estado")
            orden.instance.fechain = fecha
            init = orden.save()
            return redirect('ordenview', id=init.id)
    else:
        orden = ordenForm()

    client = Cliente.objects.get(id=client_id)

    context = {
        'fecha': fecha,
        'orden': orden,
        'client': client,
    }

    return render(request, 'ordenfill.html', context)


# Visualizacion de los datos de una Orden
def ordenview(request, id):
    orden = Orden.objects.get(id=id)
    proceso = Procesos.objects.all()
    valor = Valores.objects.all()
    product = Articulos.objects.all()
    price = int(0)
    for item in valor:
        if item.refer_id == orden.id:
            price = price + item.costo
    context = {
        'total': price,
        'product': product,
        'orden': orden,
        'proceso': proceso,
        'valor': valor,
    }
    return render(request, 'ordenview.html', context)


# Formulario para modificar una orden
def ordenupd(request, id):
    orden = Orden.objects.get(id=id)
    status = Orden.STATUS
    context = {
        'orden': orden,
        'status': status,
    }

    return render(request, "ordenupd.html", context)


# Funcion para guardar los datos modificados de una orden
def ordenmod(request, id):
    orden = get_object_or_404(Orden, id=id)

    if request.method == 'GET':
        orden = ordenForm(instance=orden)
        return redirect("ordenview", id=id)

    else:

        orden = ordenForm(request.POST, instance=orden)
        print(orden.errors)
        if orden.is_valid():
            orden.save()
            return redirect("ordenview", id=id)
        else:
            orden = clienteForm()
            return redirect("ordenview", id=id)


def orden(request, client_id, id=None):
    if id is None:
        instance = None
    else:
        instance = Orden.objects.get(id=id)

    form = ordenForm(
        data=request.POST,
        instance=instance,
    )
    if request.method == 'POST':
        if form.is_valid():
            form.instance.client_id = id
            init = form.save()
            return redirect('ordenview', id=init.id)

    client = Cliente.objects.get(id=client_id)

    context = {
        'orden': orden,
        'client': client,
    }

    return render(request, 'ordenupd.html', context)
    # return render(request, 'ordenupd.html', {})


def vdatein(request):
    if request.method=="POST":
        desde= request.POST.get("desde")
        hasta = request.POST.get("hasta")
        result = Orden.objects.raw('select id, fechain, num_orden, instrumento, encargado, estado from clientesapp_orden where fechain between "'+desde+'" and "'+hasta+'"')

        return render(request, 'vdatein.html', {'orden': result})
    else:
        orden = Orden.objects.all().order_by('fechain')

        page = request.GET.get('page', 1)

        paginator = Paginator(orden, 20)

        try:
            orden = paginator.page(page)
        except PageNotAnInteger:
            orden = paginator.page(1)
        except EmptyPage:
            orden = paginator.page(paginator.num_pages)

        context = {
            'orden': orden,
            'paginator': paginator,
        }

        return render(request, 'vdatein.html', context)


def vdateout(request):
    if request.method=="POST":
        desde= request.POST.get("desde")
        hasta = request.POST.get("hasta")
        result = Orden.objects.raw('select id, fechaout, num_orden, instrumento, encargado, estado from clientesapp_orden where fechaout between "'+desde+'" and "'+hasta+'"')

        return render(request, 'vdateout.html', {'orden': result})
    else:
        orden = Orden.objects.all().order_by('fechaout')

        page = request.GET.get('page', 1)

        paginator = Paginator(orden, 20)

        try:
            orden = paginator.page(page)
        except PageNotAnInteger:
            orden = paginator.page(1)
        except EmptyPage:
            orden = paginator.page(paginator.num_pages)

        context = {
            'orden': orden,
            'paginator': paginator,
        }

        return render(request, 'vdateout.html', context)


def informes(request):
    return render(request, 'informes.html', {})


def vprocess(request, reference_id):
    if request.method == 'POST':
        if request.POST.get('procesos'):
            addprocess = Procesos()
            addprocess.process = request.POST.get('procesos')
            addprocess.reference_id = reference_id
            addprocess.save()
        if request.POST.get('valor'):
            addcosto = Valores()
            addcosto.costo = request.POST.get('valor')
            addcosto.refer_id = reference_id
            addcosto.show_ref = '1'
            addcosto.save()
        return redirect('ordenview', id=reference_id)
    else:
        proceso = procesosForm()

    reference = Orden.objects.get(id=reference_id)
    refer = Orden.objects.get(id=reference_id)

    context = {
        'refer': refer,
        'proceso': proceso,
        'reference': reference,
    }

    return render(request, 'vprocess.html', context)


def varticles(request, referencia_id):
    if request.method == 'POST':
        if request.POST.get('articulos'):
            additem = Articulos()
            additem.articulo = request.POST.get('articulos')
            additem.orden_ref_id = referencia_id
            additem.save()
        if request.POST.get('valor'):
            addcosto = Valores()
            addcosto.costo = request.POST.get('valor')
            addcosto.refer_id = referencia_id
            addcosto.show_ref = '2'
            addcosto.save()
        return redirect('ordenview', id=referencia_id)
    else:
        article = articlesForm()

    referencia = Orden.objects.get(id=referencia_id)
    refer = Orden.objects.get(id=referencia_id)

    context = {
        'refer': refer,
        'article': article,
        'referencia': referencia,
    }

    return render(request, 'varticles.html', context)

def load_images(request, ref_guia_id):

    if request.method == "POST":
        loadim = Imagenes()
        loadim.ref_guia_id = ref_guia_id
        loadim.imagen = request.FILES['image']
        loadim.save()
        return redirect('ordenview', id=ref_guia_id)
    else:
        images = imagenesForm()

    ref_guia = Orden.objects.get(id=ref_guia_id)
    imgs = Imagenes.objects.all()

    context = {
        'imgs': imgs,
        'ref_guia': ref_guia,
        'images': images,
    }

    return render(request, 'load_images.html', context)