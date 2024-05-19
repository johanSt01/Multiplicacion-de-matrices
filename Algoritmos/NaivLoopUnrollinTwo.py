import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

def naivLoopUnrollingTwo(a, b, c, n, p, m):
    if p % 2 == 0:
        for i in range(n):
            for j in range(m):
                aux = 0.0
                for k in range(0, p, 2):
                    aux += a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j]
                c[i][j] = aux
    else:
        PP = p - 1
        for i in range(n):
            for j in range(m):
                aux = 0.0
                for k in range(0, PP, 2):
                    aux += a[i][k] * b[k][j] + a[i][k + 1] * b[k + 1][j]
                c[i][j] = aux + a[i][PP] * b[PP][j]
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
    m3 = [[0 for _ in range(m2l)] for _ in range(m1l)]

    resultado = naivLoopUnrollingTwo(m1, m2, m3, m1l, m2l, p)
    imprimirMatriz(resultado)