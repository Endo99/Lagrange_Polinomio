from sympy import *

class Lagrange:
    def achar_l(self, x_array, y_array):
        numeros = []
        x = symbols('x', integer = True)
        for i in range(len(x_array)):
            for j in range(len(y_array)):
                if i != j:
                    if i == 0:
                        l = ((x - x_array[i+1]) * (x - x[i+2]) / (x_array[0] - x_array[i+2])) # Cálcula o L0
                        numeros.append({
                            "indices": i,
                            "resultados": l
                        })
                    elif i == 1:
                        l = ((x - x_array[0]) * (x - x[i+2]) / (x_array[0] - x_array[i+2])) # Cálcula o L1
                        numeros.append({
                            "indices": i,
                            "resultados": l
                        })
        
        for numeros in numeros:
            print(f'Chave: {numeros["indices"]}, Conteúdo: {numeros["resultados"]}' )
        return numeros

    def fx(self, numeros):
        lagrange = Lagrange()
        for i in range(len(numeros)):
            f = lagrange.achar_l()