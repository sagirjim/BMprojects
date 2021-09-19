from django.shortcuts import render
from clientesapp.models import Cliente, Orden
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def showinfo(request, id):
    orden = Orden.objects.get(id=id)

    context = {
        'orden': orden,
    }
    return render(request, 'showinfo.html', context)

def pdf_create(request, id):
    orden = Orden.objects.get(id=id)

    template_path = 'showinfo.html'
    context = {'orden': orden,}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recibo.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response