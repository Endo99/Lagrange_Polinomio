import numpy as np
from tkinter import *

class Lagrange():


    def lagrange(self, x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, inter):
# Lagrange Interpolation

        x0_0 = int(x0)
        x1_1 = int(x1)
        x2_2 = int(x2)
        x3_3 = int(x3)
        x4_4 = int(x4)

        y0_0 = int(y0)
        y1_1 = int(y1)
        y2_2 = int(y2)
        y3_3 = int(y3)
        y4_4 = int(y4)

        x = [x0, x1, x2, x3, x4]
        y = [y0, y1, y2, y3, y4]

# Reading interpolation point
        xp = inter

# Set interpolated value initially to zero
        yp = 0

# Implementing Lagrange Interpolation
        for i in range(len(x)):
    
            p = 1
    
            for j in range(len(x)):
                if i != j:
                    p = p * (xp - x[j])/(x[i] - x[j])
    
            yp = yp + p * y[i]

        print('O resultado do ponto de interpolação: %.3f, é: %.3f' % (xp, yp))
