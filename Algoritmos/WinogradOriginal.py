import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

def winogradOriginal(a, b, c, n, p, m):
    upsilon = p % 2
    gamma = p - upsilon
    y = [0.0] * m
    z = [0.0] * n

    for i in range(m):
        aux = 0.0
        for j in range(0, gamma, 2):
            aux += a[i][j] * a[i][j + 1]
        y[i] = aux

    for i in range(n):
        aux = 0.0
        for j in range(0, gamma, 2):
            aux += b[j][i] * b[j + 1][i]
        z[i] = aux

    if upsilon == 1:
        PP = p - 1
        for i in range(m):
            for k in range(n):
                aux = 0.0
                for j in range(0, gamma, 2):
                    aux += (a[i][j] + b[j + 1][k]) * (a[i][j + 1] + b[j][k])
                c[i][k] = aux - y[i] - z[k] + a[i][PP] * b[PP][k]
    else:
        for i in range(m):
            for k in range(n):
                aux = 0.0
                for j in range(0, gamma, 2):
                    aux += (a[i][j] + b[j + 1][k]) * (a[i][j + 1] + b[j][k])
                c[i][k] = aux - y[i] - z[k]

    # Liberar memoria
    y = None
    z = None

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

    resultado = winogradOriginal(m1, m2, m3, m1l, m2l, p)
    imprimirMatriz(resultado)
