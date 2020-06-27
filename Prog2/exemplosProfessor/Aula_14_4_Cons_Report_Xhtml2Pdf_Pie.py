import os

import matplotlib.pyplot as plt
import base64
from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template 
from xhtml2pdf import pisa

def link_event(uri, rel):
	# Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources #
	# use short variable names
	sUrl = settings.STATIC_URL # Typically /static/
	sRoot = settings.STATIC_ROOT # Typically /home/userX/project_static/
	mUrl = settings.MEDIA_URL # Typically /static/media/
	mRoot = settings.MEDIA_ROOT # Typically /home/userX/project_static/media/
	# print("sUrl=%s\nsRoot=%s\nmUrl=%s\nmRoot=%s\nos.path=%s\nuri=%s\n" % (sUrl, sRoot, mUrl, mRoot, os.path, uri))
	
	path="%s\\%s" % (mUrl, uri.replace(".\\",""))
	print("path=%s" % path)
	return(path)

def read_html(input_filename):
	Str=""
	with open(input_filename, "r") as file:
		Data=file.readlines()
	
	for line in Data:
		Str=Str+line
	
	return(Str)

def convert_html_to_pdf(source_html, output_filename):
	result_file = open(output_filename, "w+b")
	
    # convert HTML to PDF
	pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file,           # file handle to recieve result
			link_callback=link_event)

    # close output file
	result_file.close()                 # close output file

    # return True on success and False on errors
	return pisa_status.err

def criar_figura():
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
	sizes = [15, 30, 45, 10]
	explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
	
	fig, ax = plt.subplots()
	ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	
	# plt.show()
	
	return(fig)

def inserir_figura(Str, fig):
	Bt_IO=BytesIO()
	fig.savefig(Bt_IO, format='png')
	Data=base64.b64encode(Bt_IO.getvalue()).decode("ascii")
	Aux="<image border='1' src='data:image/png;base64,%s'>" % (Data)
	
	Str=Str.replace("<Figure></Figure>", Aux)
	
	return(Str)

################################################################################

print("\n\n",os.getcwd())

settings.configure()

settings.STATIC_URL=os.getcwd()
settings.STATIC_ROOT=os.getcwd()
settings.MEDIA_URL="%s\\Html_Report" % (os.getcwd())
mRoot = settings.MEDIA_ROOT="%s\\Html_Report" % (os.getcwd())

Str=read_html("./Html_Report/Grafico.html")
print("Reading: './Html_Report/Grafico.html'")

################################

fig=criar_figura()
Str=inserir_figura(Str, fig)

################################

convert_html_to_pdf(Str, './Html_Report/Report_04_Pie.pdf')
print("Creating: './Html_Report/Report_04_Pie.pdf'")