import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
# Fixing random state for reproducibility
np.random.seed(19680801)

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
	N_points = 100000
	n_bins = 20
	
	# Generate a normal distribution, center at x=0 and y=5
	x = np.random.randn(N_points)
	y = .4 * x + np.random.randn(100000) + 5
	
	fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
	
	# We can set the number of bins with the `bins` kwarg
	axs[0].hist(x, bins=n_bins)
	axs[1].hist(y, bins=n_bins)
	
	fig, axs = plt.subplots(1, 2, tight_layout=True)
	
	# N is the count in each bin, bins is the lower-limit of the bin
	N, bins, patches = axs[0].hist(x, bins=n_bins)
	
	# We'll color code by height, but you could use any scalar
	fracs = N / N.max()
	
	# we need to normalize the data to 0..1 for the full range of the colormap
	norm = colors.Normalize(fracs.min(), fracs.max())
	
	# Now, we'll loop through our objects and set the color of each accordingly
	for thisfrac, thispatch in zip(fracs, patches):
		color = plt.cm.viridis(norm(thisfrac))
		thispatch.set_facecolor(color)
	
	# We can also normalize our inputs by the total number of counts
	axs[1].hist(x, bins=n_bins, density=True)
	
	# Now we format the y-axis to display percentage
	axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))
	
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

convert_html_to_pdf(Str, './Html_Report/Report_05_Hist.pdf')
print("Creating: './Html_Report/Report_05_Hist.pdf'")