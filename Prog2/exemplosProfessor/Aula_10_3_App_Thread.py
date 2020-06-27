from tkinter import *
import threading
import time

class Janela_App():
    def __init__(self, Master, Str="Janela", x1="0", y1="0", dx="640", dy="480", cor="ligthgray"):
        self.Master = Master
        self.Master.title(Str)
        self.Master.geometry("%sx%s+%s+%s" % (dx, dy, x1, y1))
        self.Master.configure(bg=cor)
        self.inicialize(self.Master)

    def run1(self, threadName, delay):
        count = 0
        while count < self.total1:
            count += 1
            self.lock.acquire()
            self.Txt1.insert(END, "<Este é o %s ..." % (threadName))
            self.Txt1.insert(END, "e está com valor de count=%d " % (count))
            self.Txt1.insert(END, "..............................>\n")
            self.lock.release()
            time.sleep(delay)

    def run2(self, threadName, delay):
        count = 0
        while count < self.total2:
            count += 1
            self.lock.acquire()
            self.Txt1.insert(END, "<Este é o %s ..." % (threadName))
            self.Txt1.insert(END, "e está com valor de count=%d " % (count))
            self.Txt1.insert(END, "..............................>\n")
            self.lock.release()
            time.sleep(delay)

    def run3(self, threadName, delay):
        count = 0
        while count < self.total3:
            count += 1
            self.lock.acquire()
            self.Txt1.insert(END, "<Este é o %s ..." % (threadName))
            self.Txt1.insert(END, "e está com valor de count=%d " % (count))
            self.Txt1.insert(END, "..............................>\n")
            self.lock.release()
            time.sleep(delay)

    def action_Thread1(self):
        try:
            if (self.thr1 is None):
                self.total1=3000
                self.thr1=threading.Thread(target=self.run1, args=["Processo N.1", 0.2])
                self.thr1.start()
            else:
                self.total1=0
                self.thr1=None
        except Exception as ex:
            print("Error: unable to start thread: %s\n%s\n" % ("Processo N.1",ex))

    def action_Thread2(self):
        try:
            if (self.thr2 is None):
                self.total2=3000
                self.thr2=threading.Thread(target=self.run2, args=["Processo N.2", 0.1])
                self.thr2.start()
            else:
                self.total2=0
                self.thr2=None
        except Exception as ex:
            print("Error: unable to start thread: %s\n%s\n" % ("Processo N.2",ex))

    def action_Thread3(self):
        try:
            if (self.thr3 is None):
                self.total3=3000
                self.thr3=threading.Thread(target=self.run3, args=["Processo N.3", 0.05])
                self.thr3.start()
            else:
                self.total3=0
                self.thr3=None
        except Exception as ex:
            print("Error: unable to start thread: %s\n%s\n" % ("Processo N.3",ex))

    def inicialize(self, parent):
        Sb1 = Scrollbar(parent, orient="vertical")
        self.Txt1=Text(parent, height=59, width=96, yscrollcommand=Sb1.set)
        Sb1.config(command=self.Txt1.yview)

        self.total1=300;
        self.total2=300;
        self.total3=300;

        self.thr1=None
        self.thr2=None
        self.thr3=None
        self.lock = threading.Lock()

        Bt1=Button(parent, text='Processo N.1', command=self.action_Thread1)
        Bt2=Button(parent, text='Processo N.2', command=self.action_Thread2)
        Bt3=Button(parent, text='Processo N.3', command=self.action_Thread3)

        Bt1.grid(row=0, column=0, sticky=N, padx=4, pady=4)
        Bt2.grid(row=0, column=1, sticky=N, padx=4, pady=4)
        Bt3.grid(row=0, column=2, sticky=N, padx=4, pady=4)
        Sb1.grid(row=1, column=3, rowspan=1, sticky=NS)

        self.Txt1.grid(row=1, column=0, columnspan=3, sticky=N, padx=4, pady=4)

Root=Tk()
Jan1 = Janela_App(Root, "Minha janela", "320", "0", "800", "1000", "orange")
Root.mainloop( )
