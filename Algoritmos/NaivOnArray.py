import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

def naive_on_array(a, b, c, n, p, m):
    for i in range(n):
        for j in range(m):
            c[i][j] = 0.0
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]
    return c

def imprimir_matriz(matriz):
    imprimir = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            imprimir += " " + str(matriz[i][j])
        imprimir += "\n"
    print(imprimir)

def main():
    m1= Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 1.xml").getMatriz()
    m2 = Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 2.xml").getMatriz()
    m1l = len(m1)
    m2l = len(m2)
    p = len(m2[0])
    m3 = [[0 for _ in range(m2l)] for _ in range(m1l)]

    resultado = naive_on_array(m1, m2, m3, m1l, m2l, p)
    imprimir_matriz(resultado)

if __name__ == "__main__":
    main()
