from tkinter import *
from tkinter.font import Font


root = Tk()
root.title('Método de Lagrange')
root.geometry('600x600')
root['bg'] = 'gray'

fontStyle = Font(family='Arial', size=15)
fontStyle1 = Font(family='Arial', size=12)

legenda = Label(root, text='Método de Lagrange desenvolvido por Maria Isabelly e Wellington Endo',
background='gray', foreground='white', font=fontStyle1)
legenda.place(x=50, y=50)

def tamanho4():
        

        def lagrange4():
        
                root['bg'] = 'gray'
                x0_0 = float(x0.get())
                y0_0 = float(y0.get())

                x1_1 = float(x1.get())
                y1_1 = float(y1.get())
                        
                x2_2 = float(x2.get())
                y2_2 = float(y2.get())
                        
                x3_3 = float(x3.get())
                y3_3 = float(y3.get())

                inter_a = float(inter.get())

                x = [x0_0, x1_1, x2_2, x3_3]
                y = [y0_0, y1_1, y2_2, y3_3]
                        
                xp = inter_a

                        
                yp = 0
                        
                for i in range(len(x)):
                
                        p = 1
                
                        for j in range(len(x)):
                                if i != j:
                                        p = p * (xp - x[j])/(x[i] - x[j])
                
                        yp = yp + p * y[i]


                legenda_resultado = Label(root, text="Resultado:")
                legenda_resultado.place(x=250, y=350)

                resultado = Label(root, text="O resultado do ponto de interpolação de %0.3f, é: %.3f" % (xp,yp),
                bg='gray', foreground='white', font=fontStyle)
                resultado.place(x=150, y=380)

                resultado['text'] = yp

        button4.place_forget()
        button5.place_forget()
        quantidade.place_forget()

        x0 = Entry(root, width=20)
        x0.place(x=150, y=100)
        x0.insert(0, 'x0:')
        y0 = Entry(root, width=20)
        y0.place(x=300, y=100)
        y0.insert(0, 'y0:')

        x1 = Entry(root, width=20)
        x1.place(x=150, y=130)
        x1.insert(0, 'x1:')
        y1 = Entry(root, width=20)
        y1.place(x=300, y=130)
        y1.insert(0, 'y1:')

        x2 = Entry(root, width=20)
        x2.place(x=150, y=160)
        x2.insert(0, 'x2:')
        y2 = Entry(root, width=20)
        y2.place(x=300, y=160)
        y2.insert(0, 'y2:')

        x3 = Entry(root, width=20)
        x3.place(x=150, y=190)
        x3.insert(0, 'x3:')
        y3 = Entry(root, width=20)
        y3.place(x=300, y=190)
        y3.insert(0, 'y3:')

        inter = Entry(root, width=20)
        inter.place(x=150, y=220)
        inter.insert(0, 'Entre com uma valor de interpolação:')

        button_incial = Button(root, text='Calcular',
                command=lagrange4, padx=10, pady=10)
        button_incial.place(x=250, y=280)

                
def tamanho5():

        def lagrange5():
        
                root['bg'] = 'gray'
                x0_0 = float(x0.get())
                y0_0 = float(y0.get())

                x1_1 = float(x1.get())
                y1_1 = float(y1.get())
                        
                x2_2 = float(x2.get())
                y2_2 = float(y2.get())
                        
                x3_3 = float(x3.get())
                y3_3 = float(y3.get())
                        
                x4_4 = float(x4.get())
                y4_4 = float(y4.get())

                inter_a = float(inter.get())

                x = [x0_0, x1_1, x2_2, x3_3, x4_4]
                y = [y0_0, y1_1, y2_2, y3_3, y4_4]
                        
                xp = inter_a

                        
                yp = 0
                        
                for i in range(len(x)):
                
                        p = 1
                
                        for j in range(len(x)):
                                if i != j:
                                        p = p * (xp - x[j])/(x[i] - x[j])
                
                        yp = yp + p * y[i]

                legenda_resultado = Label(root, text="Resultado:")
                legenda_resultado.place(x=250, y=350)

                resultado = Label(root, text="O resultado do ponto de interpolação de %0.3f, é: %.3f" % (xp,yp),
                bg='gray', foreground='white', font=fontStyle)
                resultado.place(x=150, y=380)

                resultado['text'] = yp


        button5.place_forget()
        button4.place_forget()
        quantidade.place_forget()
                
        x0 = Entry(root, width=20)
        x0.place(x=150, y=100)
        x0.insert(0, 'x0:')
        y0 = Entry(root, width=20)
        y0.place(x=300, y=100)
        y0.insert(0, 'y0:')

        x1 = Entry(root, width=20)
        x1.place(x=150, y=130)
        x1.insert(0, 'x1:')
        y1 = Entry(root, width=20)
        y1.place(x=300, y=130)
        y1.insert(0, 'y1:')

        x2 = Entry(root, width=20)
        x2.place(x=150, y=160)
        x2.insert(0, 'x2:')
        y2 = Entry(root, width=20)
        y2.place(x=300, y=160)
        y2.insert(0, 'y2:')

        x3 = Entry(root, width=20)
        x3.place(x=150, y=190)
        x3.insert(0, 'x3:')
        y3 = Entry(root, width=20)
        y3.place(x=300, y=190)
        y3.insert(0, 'y3:')

        x4 = Entry(root, width=20)
        x4.place(x=150, y=220)
        x4.insert(0, 'x4:')
        y4 = Entry(root, width=20)
        y4.place(x=300, y=220)
        y4.insert(0, 'y4:')

        inter = Entry(root, width=20)
        inter.place(x=150, y=250)
        inter.insert(0, 'Entre com uma valor de interpolação:')

        button_incial = Button(root, text='Calcular',
                command=lagrange5, padx=10, pady=10)
        button_incial.place(x=250, y=280)


quantidade = Label(root, text='Click na quantidade desejada: ', bg='gray', foreground='white', font=fontStyle)
quantidade.place(x=150, y=150, width=280, height=60)

button4 = Button(root, text='4',
                       command=tamanho4, padx=10, pady=10, bg='black', foreground='white')
button4.place(x=200, y=210, width=60, height=60)
#la.lagrange(x0.get(), x1.get())

button5 = Button(root, text='5',
                       command=tamanho5, padx=10, pady=10, bg='black', foreground='white')
button5.place(x=300, y=210, width=60, height=60)


root.mainloop()
