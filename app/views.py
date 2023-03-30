from django.urls import reverse_lazy
from django.views import generic

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404


import datetime 
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from datetime import datetime
from app.models import ExampleModel


class ExampleCreateView(generic.CreateView):
    model = ExampleModel
    fields = '__all__'
    success_url = reverse_lazy('list')


class ExampleUpdateView(generic.UpdateView):
    model = ExampleModel
    fields = '__all__'
    success_url = reverse_lazy('list')


class ExampleListView(generic.ListView):
    model = ExampleModel

import base64


from django.conf import settings
from .models import ExampleModel
from .utils import signature_base64, signature_2base64
def generate_pdf(request, id):
    response = HttpResponse(content_type='application/pdf')
    d = datetime.today().strftime('%Y-%m-%d')
    response['Content-Disposition']= 'inline; filename="[{filename}].pdf"'.format(filename=d)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    #Data to print
    data = {
        "Posts":[{"title" : "Python", "views ":300}, {"title" : "JavaScript", "views " :800}],
        "Videos":[{"title" : "Python Programming", "likes":580}],
        "Blogs": [{"name": "Report Lab", "Likes": 400, "claps": 900}],
    }
    
    # Start writing the PDF here
    pdfmetrics.registerFont(TTFont('ARIALUNI',('%s/Fonts/ARIALUNI.ttf'%(settings.STATIC_ROOT))))
    pdfmetrics.registerFont(TTFont('ARIALNB',('%s/Fonts/ARIALNB.ttf'%(settings.STATIC_ROOT))))
    p.setFont("ARIALUNI", 12, leading=None)
    p.setFillColorRGB(0.29296875, 0.453125,0.609375)
    p.drawString(260,760, "Report Data")
    # p.line(0,780,1500,780)

    x1 = 80
    y1 = 750

    obj = get_object_or_404(ExampleModel, pk=id) 
    image64 = signature_2base64(obj.signature)
    
    decoded_data=base64.b64decode(image64)

    filename = '%s/signature/%s.png'%(settings.MEDIA_ROOT, id)
    img_file = open(filename, 'wb')
    img_file.write(decoded_data)
    img_file.close()
    # print ( image64 )  


    
   
    #Render data
    for k,v in data.items():
        for value in v:
            for key,val in value.items():
                p.setFont("Helvetica",10,leading=None)
                p.drawString(x1, y1-20, f"{key} - {val}")
                y1 = y1-70

    # p.drawImage(signature, 10, 10, mask='auto')
    # p.drawImage(signature, 50, 50, 50, 50, preserveAspectRatio=True, anchor='c')

    # for i in range(1,39):
    #     p.drawString(i*20, 200, "{value}".format(value=i))
    #     p.drawString(i*20, 185, "{value}".format(value="^"))   

    for i in range(1,59):
        p.drawString(i*10, 15, "{value}".format(value=i))
        p.drawString(i*10, 5, "{value}".format(value="V"))        

    # p.roundRect(165, 40, 255, 50, 4, stroke=1, fill=0) #x, y, width, height

    signature = ImageReader("media/signature/{filename}.png".format(filename=id))    
    p.drawImage(signature, 250, 5, width=2*inch, preserveAspectRatio=True, mask='auto')

    p.setFont("ARIALUNI", 12, leading=None)    
    p.drawString(270, 40, "Signature")    
    # p.line(0,30,1000,30)    

    p.setTitle("Report on {filename}".format(filename=d))
    
    p.showPage()
    p.save()
    

    buffer.seek(0)
    newPdf = PdfFileReader(buffer)
            


    # #######DEBUG NEW PDF created#############
    pdf1 = buffer.getvalue()
    open((settings.MEDIA_ROOT + '/signature/pdf_buf{id}.pdf').format(id=id), 'wb').write(pdf1)
    
    # #########################################

    # read your PDF template
    pdf_template = settings.MEDIA_ROOT + '/signature/template.pdf'
    existingPdf = PdfFileReader(open(pdf_template, 'rb'))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existingPdf.getPage(0)
    page.mergePage(newPdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    
    filename = settings.MEDIA_ROOT + '/signature/{name}.pdf'.format(name=id)

    outputStream =  open(filename, 'wb')
    output.write(outputStream)
    outputStream.close()
    
    outputStream =  open(filename, 'wb')
    output.write(outputStream)
    outputStream.close()

    try:             
        return FileResponse(open(filename, 'rb')) 
    except FileNotFoundError:
        raise Http404()
        

