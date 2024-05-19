import math
import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

class StrassenWinograd:
    def max(self, n, p):
        if n < p:
            return p
        else:
            return n

    def strassenWinograd(self, a, b, c, n, p, m):
        MaxSize = self.max(n, p)
        MaxSize = self.max(MaxSize, m)

        if MaxSize < 16:
            MaxSize = 16

        k = int(math.floor(math.log(MaxSize) / math.log(2)) - 4)
        mm = int(math.floor(MaxSize * 2 ** -k)) + 1
        NewSize = mm * 2 ** k

        # Agregar filas y columnas de cero para utilizar el algoritmo de Strassen
        NewA = [[0.0] * NewSize for _ in range(NewSize)]
        NewB = [[0.0] * NewSize for _ in range(NewSize)]
        AuxResult = [[0.0] * NewSize for _ in range(NewSize)]

        for i in range(n):
            for j in range(p):
                NewA[i][j] = a[i][j]

        for i in range(p):
            for j in range(m):
                NewB[i][j] = b[i][j]

        self.strassenWinogradStep(NewA, NewB, AuxResult, NewSize, mm)

        # Extraer el resultado
        for i in range(n):
            for j in range(m):
                c[i][j] = AuxResult[i][j]

        return c

    def minus(self, a, b, c, n, m):
        for i in range(n):
            for j in range(m):
                c[i][j] = a[i][j] - b[i][j]

    def plus(self, a, b, c, n, m):
        for i in range(n):
            for j in range(m):
                c[i][j] = a[i][j] + b[i][j]

    def strassenWinogradStep(self, a, b, c, n, m):
        if n % 2 == 0 and n > m:
            NewSize = n // 2

            A1 = [[0.0] * NewSize for _ in range(NewSize)]
            A2 = [[0.0] * NewSize for _ in range(NewSize)]
            B1 = [[0.0] * NewSize for _ in range(NewSize)]
            B2 = [[0.0] * NewSize for _ in range(NewSize)]

            A11 = [[0.0] * NewSize for _ in range(NewSize)]
            A12 = [[0.0] * NewSize for _ in range(NewSize)]
            A21 = [[0.0] * NewSize for _ in range(NewSize)]
            A22 = [[0.0] * NewSize for _ in range(NewSize)]
            B11 = [[0.0] * NewSize for _ in range(NewSize)]
            B12 = [[0.0] * NewSize for _ in range(NewSize)]
            B21 = [[0.0] * NewSize for _ in range(NewSize)]
            B22 = [[0.0] * NewSize for _ in range(NewSize)]

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
            Aux8 = [[0.0] * NewSize for _ in range(NewSize)]
            Aux9 = [[0.0] * NewSize for _ in range(NewSize)]

            for i in range(NewSize):
                for j in range(NewSize):
                    A11[i][j] = a[i][j]
                    A12[i][j] = a[i][NewSize + j]
                    A21[i][j] = a[NewSize + i][j]
                    A22[i][j] = a[NewSize + i][NewSize + j]
                    B11[i][j] = b[i][j]
                    B12[i][j] = b[i][NewSize + j]
                    B21[i][j] = b[NewSize + i][j]
                    B22[i][j] = b[NewSize + i][NewSize + j]

            self.minus(A11, A21, A1, NewSize, NewSize)
            self.minus(A22, A1, A2, NewSize, NewSize)
            self.minus(B22, B12, B1, NewSize, NewSize)
            self.plus(B1, B11, B2, NewSize, NewSize)

            self.strassenWinogradStep(A11, B11, Aux1, NewSize, m)
            self.strassenWinogradStep(A12, B21, Aux2, NewSize, m)
            self.strassenWinogradStep(A2, B2, Aux3, NewSize, m)
            self.plus(A21, A22, Helper1, NewSize, NewSize)
            self.minus(B12, B11, Helper2, NewSize, NewSize)
            self.strassenWinogradStep(Helper1, Helper2, Aux4, NewSize, m)
            self.strassenWinogradStep(A1, B1, Aux5, NewSize, m)
            self.minus(A12, A2, Helper1, NewSize, NewSize)
            self.strassenWinogradStep(Helper1, B22, Aux6, NewSize, m)
            self.minus(B21, B2, Helper1, NewSize, NewSize)
            self.strassenWinogradStep(A22, Helper1, Aux7, NewSize, m)
            self.plus(Aux1, Aux3, Aux8, NewSize, NewSize)
            self.plus(Aux8, Aux4, Aux9, NewSize, NewSize)

            self.plus(Aux1, Aux2, ResultPart11, NewSize, NewSize)
            self.plus(Aux9, Aux6, ResultPart12, NewSize, NewSize)
            self.plus(Aux8, Aux5, Helper1, NewSize, NewSize)
            self.plus(Helper1, Aux7, ResultPart21, NewSize, NewSize)
            self.plus(Aux9, Aux5, ResultPart22, NewSize, NewSize)

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

            # Liberar variables auxiliares
            A1 = None
            A2 = None
            B1 = None
            B2 = None

            A11 = None
            A12 = None
            A21 = None
            A22 = None

            B11 = None
            B12 = None
            B21 = None
            B22 = None

            ResultPart11 = None
            ResultPart12 = None
            ResultPart21 = None
            ResultPart22 = None

            Helper1 = None
            Helper2 = None

            Aux1 = None
            Aux2 = None
            Aux3 = None
            Aux4 = None
            Aux5 = None
            Aux6 = None
            Aux7 = None

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
    strassenWinograd = StrassenWinograd()

    resultado = strassenWinograd.strassenWinograd(m1, m2, m3, m1l, m2l, p)
    imprimirMatriz(resultado)
