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


        lbNome.place(x=0,y=10)
        lbTel.place(x=0,y=30)
        lbEmail.place(x=0,y=50)
        lbEnd.place(x=0,y=70)


        etNome.place(x=200,y=10)
        etTel.place(x=200,y=30)
        etEmail.place(x=200,y=50)
        etEnd.place(x=200,y=70)


root = janela()
root.mainloop()
