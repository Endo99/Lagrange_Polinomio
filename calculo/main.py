from lagrange import Lagrange
from sympy import *

if __name__ == '__main__':
    lagrange = Lagrange()

    i = 0

    vetor = []
    aux_vetor = []


    while i <= 3:

        x = float(input('Digite um valor para X: \n'))
        vetor.append(x)
        y = float(input("Digite um valor para Y: \n"))
        aux_vetor.append(y)

        i += 1
        
    salvar = lagrange.achar_l(vetor, aux_vetor)

    print(salvar)
