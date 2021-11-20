from tkinter import *
from lagrange import Lagrange


root = Tk()
root.geometry('500x500')
root.resizable(width=500, height=500)

def entradas():

        la = Lagrange()

        x0 = Entry(root, width=20)
        x0.pack()
        y0 = Entry(root, width=20)
        y0.pack()

        x1 = Entry(root, width=20)
        x1.pack()
        y1 = Entry(root, width=20)
        y1.pack()

        x2 = Entry(root, width=20)
        x2.pack()
        y2 = Entry(root, width=20)
        y2.pack()

        x3 = Entry(root, width=20)
        x3.pack()
        y3 = Entry(root, width=20)
        y3.pack()

        x4 = Entry(root, width=20)
        x4.pack()
        y4 = Entry(root, width=20)
        y4.pack()

        inter = Entry(root, width=20)
        inter.pack()

        la.lagrange(x0.get(), y0.get(), x1.get(), y1.get(), x2.get(), y2.get(), x3.get(), y3.get(),
        x4.get(), y4.get(), inter.get())

button_incial = Button(root, 'Clique aqui para iniciar!', command=entradas())

#la.lagrange(x0.get(), x1.get())


root.mainloop()