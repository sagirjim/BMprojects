from django.shortcuts import render
from clientesapp.models import Cliente, Orden
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import xlwt
import datetime


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


def excel_create(request, id):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="recibo.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('recibo', cell_overwrite_ok=True)

    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold=True

    columns = ['Orden', 'Cliente', 'Entrada', 'Instrumento', 'Marca', 'Referencia', 'Serial', 'Encargado', 'Abono']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Orden.objects.values_list('num_orden', 'client', 'fechain', 'instrumento', 'marca',
                                     'referencia', 'serial', 'encargado', 'abono').get(id=id)
    name = Orden.objects.get(id=id)
    cliente = name.client.nombre

    row_num += 1
    for col_num in range(len(rows)):
        if col_num==1:
            ws.write(row_num, col_num, cliente, font_style)
        else:
            if columns[3]:
                ws.write(row_num, col_num, rows[col_num], date_format)
            else:
                ws.write(row_num, col_num, rows[col_num], font_style)

    wb.save(response)
    return response