from tkinter import *
import webview
import threading

## Não funcionou

def load_html():
	webview.load_html('<h1>This is dynamically loaded HTML</h1>')

def new_window():
    Jan2=Janela2("Minha janela", "600", "400", "340", "280", "cyan")

class Janela2(Frame):
    def __init__(self, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="ligthgray"):
        Top=Toplevel(Jan1)
        Frame.__init__(self, Top)
        Top.title(Str)
        Top.geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        Top.configure(bg=cor)
        self.inicialize(Top)

    def inicialize(self, parent):
        Lb1=Label(parent, text="First Name")
        Lb1.grid(row=0, column=0)
        t = threading.Thread(target=load_html)
        t.start()
        webview.create_window('Load HTML Example')

        webview.create_window("Meu navegador", "./Nota_Fiscal.html", width=800, height=600, resizable=True, fullscreen=False)
        webview.load_url("./Nota_Fiscal.html")

class Janela_App(Frame):
    def __init__(self, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="ligthgray"):
        Root=Tk()
        Frame.__init__(self, Root)
        Root.title(Str)
        Root.geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        Root.configure(bg=cor)
        self.inicialize(Root)

    def inicialize(self, parent):
        Lb1=Label(parent, text="First Name")
        Lb2=Label(parent, text="Last Name")
        Lb3=Label(parent, text="Text área")

        Et1=Entry(parent, width=52)
        Et2=Entry(parent, width=52)

        Txt1=Text(parent, height=8, width=40)

        Bt1=Button(parent, text='Quit', command=self.quit)
        Bt2=Button(parent, text='New window', command=new_window)
		
        Lb1.grid(row=0, column=0)
        Lb2.grid(row=1, column=0)
        Lb3.grid(row=3, column=0)
        Et1.grid(row=0, column=1, columnspan=2)
        Et2.grid(row=1, column=1, columnspan=2)
        Txt1.grid(row=3, column=1, columnspan=2)
        Bt1.grid(row=4, column=1, sticky=E, padx=4, pady=4)
        Bt2.grid(row=4, column=2, sticky=W, padx=4, pady=4)

Jan1 = Janela_App("Minha janela", "400", "200", "540", "380", "orange")
Jan1.mainloop( )
