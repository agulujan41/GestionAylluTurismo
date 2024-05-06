from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import os
# Create your views here.
def export_pdf(request):
    HTML('./GestionAPP/ReportsTemplates/report.html').write_pdf('./GestionAPP/ReportsTemplates/Outputs/example.pdf')
   
    current_working_directory = os.getcwd()

    # print output to the console
    current_working_directory = current_working_directory.replace('\\','/')
    filename = current_working_directory+"/GestionAPP/ReportsTemplates/Outputs/example.pdf"
    #return FileResponse(buffer, as_attachment=True, filename=filename)
    if os.path.exists(filename):
        # Abrir el archivo PDF
        with open(filename, 'rb') as pdf_file:
            # Devolver el archivo PDF como respuesta
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="archivo.pdf"'
            return response
    else:
        # Si el archivo no existe, devolver una respuesta de error
        return HttpResponse("El archivo PDF no existe", status=404)

def bouchers_customize(request):
    if request.POST:
        pass

    return render(request,"fill_boucher.html",{})