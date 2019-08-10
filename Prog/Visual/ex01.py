from tkinter import *


class janela(Tk):
    def __init__(self):
        super().__init__()
        self.title('Janela Principal')
        self.minsize(550, 150)
        self.configure(bg='#888')
        self.inicialize()

    def inicialize(self):
        lbNome = Label(text='Nome:')
        lbTel = Label(text='Telefone:')
        lbEmail = Label(text='Email:')
        lbEnd = Label(text='Endereço:')

        etNome = Entry()
        etTel = Entry()
        etEmail = Entry()
        etEnd = Entry()

        lbNome.config(width=25, height=1,font=(None, 10))
        lbTel.config(width=25, height=1, font=(None, 10))
        lbEmail.config(width=25, height=1, font=(None, 10))
        lbEnd.config(width=25, height=1, font=(None, 10))


        etEmail.config(width=50)
        etNome.config(width=50)
        etTel.config(width=50)
        etEnd.config(width=50)


        lbNome.grid(row=0, column=0, pady=10, padx=5, sticky=W)
        lbTel.grid(row=1, column=0, pady=10, padx=5, sticky=W)
        lbEmail.grid(row=2, column=0, pady=10, padx=5, sticky=W)
        lbEnd.grid(row=3, column=0, pady=10, padx=5, sticky=W)


        etNome.grid(row=0, column=1)
        etTel.grid(row=1, column=1)
        etEmail.grid(row=2, column=1)
        etEnd.grid(row=3, column=1)


root = janela()
root.mainloop()
