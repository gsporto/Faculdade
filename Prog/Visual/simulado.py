from tkinter import *


class janela(Tk):
    def __init__(self, a=400, b=400, st='title'):
        super().__init__()
        self.minsize(a, b)
        self.title(st)
        self.config(bg='#888')
        self.inicialize()
    
    def inicialize(self):
        self.__Lb_flamengo = Label(self, text='Flamengo', width=22)
        self.__Lb_vasco = Label(self, text='Vasco', width=22)
        self.__Lb_pr = Label(self, text='Paraná', width=22)
        self.__Lb_sc = Label(self, text='Santa Catarina', width=22)
        self.__Lb_rs = Label(self, text='Rio Grande Do Sul', width=22)
        self.__Lb_torcida_total = Label(self, text='Torcida Total', width=22)

        self.__Et_flamengo_pr = Entry(self, width=22)
        self.__Et_flamengo_sc = Entry(self, width=22)
        self.__Et_flamengo_rs = Entry(self, width=22)
        self.__Et_vasco_pr = Entry(self, width=22)
        self.__Et_vasco_sc = Entry(self, width=22)
        self.__Et_vasco_rs = Entry(self, width=22)
        self.__Et_total_flamengo = Entry(self, width=22)
        self.__Et_total_vasco = Entry(self, width=22)

        self.__btCalc = Button(self, text='Calcular', command= self.actionBtCal)

        self.__Lb_flamengo.grid(row=0, column=1, padx=4, pady=4, sticky=N)
        self.__Lb_vasco.grid(row=0, column=2, padx=4, pady=4, sticky=N)
        self.__Lb_pr.grid(row=1, column=0, padx=4, pady=4)
        self.__Lb_sc.grid(row=2, column=0, padx=4, pady=4)
        self.__Lb_rs.grid(row=3, column=0, padx=4, pady=4)
        self.__Lb_torcida_total.grid(row=5, column=0, padx=4, pady=4, sticky=NW)

        self.__Et_flamengo_pr.grid(row=1, column=1, padx=4, pady=4, sticky=NW)
        self.__Et_flamengo_sc.grid(row=2, column=1, padx=4, pady=4, sticky=NW)
        self.__Et_flamengo_rs.grid(row=3, column=1, padx=4, pady=4, sticky=NW)

        self.__Et_vasco_pr.grid(row=1, column=2, padx=4, pady=4, sticky=NW)
        self.__Et_vasco_sc.grid(row=2, column=2, padx=4, pady=4, sticky=NW)
        self.__Et_vasco_rs.grid(row=3, column=2, padx=4, pady=4, sticky=NW)

        self.__Et_total_flamengo.grid(row=5, column=1, padx=4, pady=4, sticky=NW)
        self.__Et_total_vasco.grid(row=5, column=2, padx=4, pady=4, sticky=NW)

        self.__btCalc.grid(row=4, column=2, padx=4, pady=4, sticky=NW)

    def actionTotalFla(self):
        self.__Et_total_flamengo.insert(END,float(self.__Et_flamengo_pr.get())+float(self.__Et_flamengo_sc.get())+float(self.__Et_flamengo_rs.get()))

    def actionTotalVas(self):
        self.__Et_total_vasco.insert(END,float(self.__Et_vasco_pr.get())+float(self.__Et_vasco_sc.get())+float(self.__Et_vasco_rs.get()))

    def actionBtCal(self):
        self.actionTotalFla()
        self.actionTotalVas()

jan1 = janela(100,100,'python')
jan1.mainloop()