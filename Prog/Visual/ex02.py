from tkinter import *


class janela(Tk):
    def __init__(self):
        super().__init__()
        self.title('Janela Principal')
        self.minsize(400, 400)
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

        lbNome.grid(row=0, column=0, pady=10, padx=5, sticky=W)
        lbDesc.grid(row=1, column=0, columnspan=2, pady=1, padx=5, sticky=W)
        lbData.grid(row=3, column=0, pady=10, padx=5, sticky=W)

        etNome.grid(row=0, column=1, pady=1, padx=2, sticky=W)
        txDesc.grid(row=2, column=0,columnspan=2, pady=1, padx=5, sticky=W)
        etData.grid(row=3, column=1, pady=1, padx=2, sticky=W)


root = janela()
root.mainloop()
