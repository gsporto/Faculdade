from tkinter import *


class janela(Tk):
    def __init__(self):
        super().__init__()
        self.title('Janela Principal')
        self.minsize(500, 500)
        self.configure(bg='#888')
        self.inicialize()

    def inicialize(self):
        lbNome = Label(text='Nome:')
        lbDesc = Label(text='Descrição:')
        lbData = Label(text='Data/Cidade')

        etNome = Entry()
        txDesc = Text()
        etData = Entry()

        lbNome.config(width=44, height=1,font=(None, 10))
        lbDesc.config(width=90, height=1, font=(None, 10))
        lbData.config(width=44, height=1,font=(None, 10))

        etNome.config(width=43)
        txDesc.config(width=90,height = 25)
        etData.config(width=43)

        lbNome.place(x=0,y=0)
        lbDesc.place(x=0,y=20)
        lbData.place(x=0,y=325)

        etNome.place(x=325,y=0)
        txDesc.place(x=0,y=40)
        etData.place(x=325,y=325)


root = janela()
root.mainloop()
