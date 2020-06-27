from tkinter import *
from tkinter import messagebox
import socket
import threading
import time

class Janela_App():
    def __init__(self, Master, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="ligthgray"):
        self.Master=Master
        self.Master.title(Str)
        self.Master.geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        self.Master.configure(bg=cor)
        self.inicialize(self.Master)

    def run(self):
        self.Txt1.insert(END, "Tentando conexão...\n")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 4000))
        hostname = socket.gethostname()
        self.Txt1.insert(END, "Conectado em: %s\n" % hostname);
        self.Txt1.insert(END, "Iniciado o fluxo de entrada/saida.\n");

        buff=""
        while (buff != "SERVIDOR>> Fim"):
            try:
                buff=self.client_socket.recv(128)
                if len(buff) > 0:
                    self.Txt1.insert(END, "%s\n" % buff.decode('UTF-8'))
            except Exception as ex:
                print("Unknown object type received: %s" % ex)
            print("11111")
            time.sleep(0.9)
        self.Txt1.insert(END, "Servidor fechou a conexao.\n")
        self.client_socket.close()

    def action_Button(self):
        try:
            if not(self.thr1 is None):
                Str1=self.Et1.get()
                byt=Str1.encode('UTF-8')
                # byt=bytes(Str1, 'UTF-8')
                self.client_socket.send(byt)
                n=len(self.Et1.get())
                self.Et1.delete(0, n)
                self.Txt1.insert(END, "%s\n" % Str1)
        except Exception as ex:
            print("Error: unable to send string: %s\n" % ex)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            print("Destruindo janela...")
            self.sair1=True
            self.Master.destroy()
            self.Master.quit()
            sys.exit(0)

    def inicialize(self, parent):
        Sb1 = Scrollbar(parent, orient="vertical")
        self.Txt1=Text(parent, height=18, width=56, yscrollcommand=Sb1.set)
        Sb1.config(command=self.Txt1.yview)

        self.sair1=False;
        self.thr1=threading.Thread(target=self.run)
        self.thr1.start()

        self.Et1=Entry(parent, width=56)
        Bt1=Button(parent, text='Enviar', command=self.action_Button)

        self.Txt1.grid(row=0, column=0, columnspan=2, sticky=N, padx=2, pady=2)
        Sb1.grid(row=0, column=2, rowspan=1, sticky=NS, padx=2, pady=2)
        self.Et1.grid(row=1, column=0, sticky=EW, padx=2, pady=2)
        Bt1.grid(row=1, column=1, sticky=EW, padx=2, pady=2)

        parent.protocol("WM_DELETE_WINDOW", self.on_closing)

Root=Tk()
Jan1 = Janela_App(Root, "Cliente", "620", "0", "480", "330", "orange")
Root.mainloop()
