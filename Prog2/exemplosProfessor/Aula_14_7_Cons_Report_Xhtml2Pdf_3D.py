import os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

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
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	
	# Make data.
	X = np.arange(-5, 5, 0.25)
	Y = np.arange(-5, 5, 0.25)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X**2 + Y**2)
	Z = np.sin(R)
	
	# Plot the surface.
	surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	
	# Customize the z axis.
	ax.set_zlim(-1.01, 1.01)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
	
	# Add a color bar which maps values to colors.
	fig.colorbar(surf, shrink=0.5, aspect=5)
	
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

convert_html_to_pdf(Str, './Html_Report/Report_07_3D.pdf')
print("Creating: './Html_Report/Report_07_3D.pdf'")