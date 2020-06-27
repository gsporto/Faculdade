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
            n=len(self.Et1.get())
            self.Et1.delete(0, n)
            self.Et1.insert(END, "%d" % count)
            time.sleep(delay)

    def run2(self, threadName, delay):
        count = 0
        while count < self.total2:
            count += 1
            n=len(self.Et2.get())
            self.Et2.delete(0, n)
            self.Et2.insert(END, "%d" % count)
            time.sleep(delay)

    def run3(self, threadName, delay):
        count = 0
        while count < self.total3:
            count += 1
            n=len(self.Et3.get())
            self.Et3.delete(0, n)
            self.Et3.insert(END, "%d" % count)
            time.sleep(delay)

    def action_Thread1(self):
        try:
            if (self.thr1 is None):
                self.total1=3000
                self.thr1=threading.Thread(target=self.run1, args=["Processo N.1", 0.4])
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
                self.thr2=threading.Thread(target=self.run2, args=["Processo N.2", 0.2])
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
                self.thr3=threading.Thread(target=self.run3, args=["Processo N.3", 0.1])
                self.thr3.start()
            else:
                self.total3=0
                self.thr3=None
        except Exception as ex:
            print("Error: unable to start thread: %s\n%s\n" % ("Processo N.3",ex))

    def inicialize(self, parent):
        self.Et1=Entry(parent, width=20)
        self.Et2=Entry(parent, width=20)
        self.Et3=Entry(parent, width=20)

        self.total1=300;
        self.total2=300;
        self.total3=300;

        self.thr1=None
        self.thr2=None
        self.thr3=None

        Bt1=Button(parent, text='Processo N.1', command=self.action_Thread1)
        Bt2=Button(parent, text='Processo N.2', command=self.action_Thread2)
        Bt3=Button(parent, text='Processo N.3', command=self.action_Thread3)

        Bt1.grid(row=0, column=0, sticky=N, padx=4, pady=4)
        Bt2.grid(row=0, column=1, sticky=N, padx=4, pady=4)
        Bt3.grid(row=0, column=2, sticky=N, padx=4, pady=4)

        self.Et1.grid(row=1, column=0, sticky=N, padx=4, pady=4)
        self.Et2.grid(row=1, column=1, sticky=N, padx=4, pady=4)
        self.Et3.grid(row=1, column=2, sticky=N, padx=4, pady=4)

Root=Tk()
Jan1 = Janela_App(Root, "Minha janela", "400", "200", "540", "380", "orange")
Root.mainloop()
