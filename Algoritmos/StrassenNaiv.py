import math
import sys
import os
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

class StrassenNaiv:
    def strassenNaiv(self, a, b, c, n, p, m):
        MaxSize = max(n, p)

        if MaxSize < 16:
            MaxSize = 16
        k = int(math.floor(math.log(MaxSize) / math.log(2)) - 4)
        mm = int(math.floor(MaxSize * 2 ** -k)) + 1
        NewSize = mm * 2 ** k

        aNew = [[0.0] * NewSize for _ in range(NewSize)]
        bNew = [[0.0] * NewSize for _ in range(NewSize)]
        auxResult = [[0.0] * NewSize for _ in range(NewSize)]

        for i in range(n):
            for j in range(p):
                aNew[i][j] = a[i][j]

        for i in range(p):
            for j in range(m):
                bNew[i][j] = b[i][j]

        self.strassenNaivStep(aNew, bNew, auxResult, NewSize, mm)

        for i in range(n):
            for j in range(m):
                c[i][j] = auxResult[i][j]
        return c

    def max(self, n, p):
        if n < p:
            return p
        else:
            return n

    def minus(self, a, b, c, n, m):
        for i in range(n):
            for j in range(m):
                c[i][j] = a[i][j] - b[i][j]

    def plus(self, a, b, c, n, m):
        for i in range(n):
            for j in range(m):
                c[i][j] = a[i][j] + b[i][j]

    def strassenNaivStep(self, a, b, c, n, m):
        if n % 2 == 0 and n > m:
            NewSize = n // 2

            A11 = [[a[i][j] for j in range(NewSize)] for i in range(NewSize)]
            A12 = [[a[i][j] for j in range(NewSize, n)] for i in range(NewSize)]
            A21 = [[a[i][j] for j in range(NewSize)] for i in range(NewSize, n)]
            A22 = [[a[i][j] for j in range(NewSize, n)] for i in range(NewSize, n)]

            B11 = [[b[i][j] for j in range(NewSize)] for i in range(NewSize)]
            B12 = [[b[i][j] for j in range(NewSize, n)] for i in range(NewSize)]
            B21 = [[b[i][j] for j in range(NewSize)] for i in range(NewSize, n)]
            B22 = [[b[i][j] for j in range(NewSize, n)] for i in range(NewSize, n)]

            ResultPart11 = [[0.0] * NewSize for _ in range(NewSize)]
            ResultPart12 = [[0.0] * NewSize for _ in range(NewSize)]
            ResultPart21 = [[0.0] * NewSize for _ in range(NewSize)]
            ResultPart22 = [[0.0] * NewSize for _ in range(NewSize)]

            Helper1 = [[0.0] * NewSize for _ in range(NewSize)]
            Helper2 = [[0.0] * NewSize for _ in range(NewSize)]

            Aux1 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux2 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux3 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux4 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux5 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux6 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux7 = [[0.0] * NewSize for _ in range(NewSize)]

            self.plus(A11, A22, Helper1, NewSize, NewSize)
            self.plus(B11, B22, Helper2, NewSize, NewSize)
            self.strassenNaivStep(Helper1, Helper2, Aux1, NewSize, m)

            self.plus(A21, A22, Helper1, NewSize, NewSize)
            self.strassenNaivStep(Helper1, B11, Aux2, NewSize, m)

            self.minus(B12, B22, Helper1, NewSize, NewSize)
            self.strassenNaivStep(A11, Helper1, Aux3, NewSize, m)

            self.minus(B21, B11, Helper1, NewSize, NewSize)
            self.strassenNaivStep(A22, Helper1, Aux4, NewSize, m)

            self.plus(A11, A12, Helper1, NewSize, NewSize)
            self.strassenNaivStep(Helper1, B22, Aux5, NewSize, m)

            self.minus(A21, A11, Helper1, NewSize, NewSize)
            self.plus(B11, B12, Helper2, NewSize, NewSize)
            self.strassenNaivStep(Helper1, Helper2, Aux6, NewSize, m)

            self.minus(A12, A22, Helper1, NewSize, NewSize)
            self.plus(B21, B22, Helper2, NewSize, NewSize)
            self.strassenNaivStep(Helper1, Helper2, Aux7, NewSize, m)

            self.plus(Aux1, Aux4, ResultPart11, NewSize, NewSize)
            self.minus(ResultPart11, Aux5, ResultPart11, NewSize, NewSize)
            self.plus(ResultPart11, Aux7, ResultPart11, NewSize, NewSize)

            self.plus(Aux3, Aux5, ResultPart12, NewSize, NewSize)

            self.plus(Aux2, Aux4, ResultPart21, NewSize, NewSize)

            self.plus(Aux1, Aux3, ResultPart22, NewSize, NewSize)
            self.minus(ResultPart22, Aux2, ResultPart22, NewSize, NewSize)
            self.plus(ResultPart22, Aux6, ResultPart22, NewSize, NewSize)

            for i in range(NewSize):
                for j in range(NewSize):
                    c[i][j] = ResultPart11[i][j]

            for i in range(NewSize):
                for j in range(NewSize):
                    c[i][NewSize + j] = ResultPart12[i][j]

            for i in range(NewSize):
                for j in range(NewSize):
                    c[NewSize + i][j] = ResultPart21[i][j]

            for i in range(NewSize):
                for j in range(NewSize):
                    c[NewSize + i][NewSize + j] = ResultPart22[i][j]

        else:
            c = self.naivStandard(a, b, c, n, n, n)
        return c

    @staticmethod
    def naivStandard(a, b, c, n, p, m):
        for i in range(n):
            for j in range(m):
                aux = 0.0
                for k in range(p):
                    aux += a[i][k] * b[k][j]
                c[i][j] = aux
        return c

def imprimirMatriz(matriz):
    imprimir = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            imprimir += " " + str(matriz[i][j])
        imprimir += "\n"
    print(imprimir)

if __name__ == "__main__":
    m1= Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 1.xml").getMatriz()
    m2 = Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 2.xml").getMatriz()
    m1l = len(m1)
    m2l = len(m2)
    p = len(m2[0])
    m3 = [[0.0] * m2l for _ in range(m1l)]
    strassenNaiv = StrassenNaiv()

    resultado = strassenNaiv.strassenNaiv(m1, m2, m3, m1l, m2l, p)
    imprimirMatriz(resultado)
