import os

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

def calcula_preco_total(preco):
	total_preco=0.0
	for i in range(0,3,1):
		total_preco=total_preco+preco[i]
	return(total_preco)

def calcula_percentual(preco, total_preco):
	percent=[]
	for i in range(0,3,1):
		percent.append(100*preco[i]/total_preco)
	return(percent)

def calcula_total_percentual(percent):
	total_perc=0.0
	for i in range(0,3,1):
		total_perc=total_perc+percent[i]
	return(total_perc)

def conteudo_dinamico_inicial(Str, quant, item, preco):
	total_preco=calcula_preco_total(preco)
	percent=calcula_percentual(preco, total_preco)
	total_perc=calcula_total_percentual(percent)
	
	Aux=""
	for i in range(0,3,1):
		Aux=Aux+"<tr>\n"
		Aux=Aux+"<td><font class='NormalFont'>%d</font></td>\n" % (i+1)
		Aux=Aux+"<td><font class='NormalFont'>%d</font></td>\n" % (quant[i])
		Aux=Aux+"<td><font class='NormalFont'>%s</font></td>\n" % (item[i])
		Aux=Aux+"<td><font class='NormalFont'>%4.2f</font></td>\n" % (preco[i])
		Aux=Aux+"<td><font class='NormalFont'>%3.1f%%</font></td>\n" % (percent[i])
		Aux=Aux+"</tr>\n"
	
	Str=Str.replace("<data_line></data_line>", Aux)
	return(Str)

def conteudo_dinamico_final(Str, quant, item, preco):
	total_preco=calcula_preco_total(preco)
	percent=calcula_percentual(preco, total_preco)
	total_perc=calcula_total_percentual(percent)
	
	Str=Str.replace("<preco_total></preco_total>", "%4.2f" % (total_preco))
	Str=Str.replace("<percentagem_total></percentagem_total>", "%3.1f%%" % (total_perc))
	return(Str)

################################################################################

print("\n\n",os.getcwd())

settings.configure()

settings.STATIC_URL=os.getcwd()
settings.STATIC_ROOT=os.getcwd()
settings.MEDIA_URL="%s\\Html_Report" % (os.getcwd())
mRoot = settings.MEDIA_ROOT="%s\\Html_Report" % (os.getcwd())

quant=[2,3,2]
item=['Livro', 'Revista', 'Jornal']
preco=[102.40, 82.60, 4.30]

# sUrl = settings.STATIC_URL # Typically /static/
# sRoot = settings.STATIC_ROOT # Typically /home/userX/project_static/
# mUrl = settings.MEDIA_URL # Typically /static/media/
# mRoot = settings.MEDIA_ROOT # Typically /home/userX/project_static/media/
# print("sUrl=%s\nsRoot=%s\nmUrl=%s\nmRoot=%s\n" % (sUrl, sRoot, mUrl, mRoot))

Str=read_html("./Html_Report/Nota_Fiscal_Tags.html")
print("Reading: './Html_Report/Nota_Fiscal_tags.html'")

Str=conteudo_dinamico_inicial(Str, quant, item, preco)
Str=conteudo_dinamico_final(Str, quant, item, preco)

## print(Str)
convert_html_to_pdf(Str, './Html_Report/Report_03_Tag.pdf')
print("Creating: './Html_Report/Report_03_Tag.pdf'")