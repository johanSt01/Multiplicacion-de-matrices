import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

def multiply2(a, b, block_size):
    size = len(a)
    c = [[0] * size for _ in range(size)]

    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(lambda _: compute_partial_result(a, b, c, size, block_size), [None])

    return c

def compute_partial_result(a, b, c, size, block_size):
    for ib in range(0, size, block_size):
        for jb in range(0, size, block_size):
            for kb in range(0, size, block_size):
                for i in range(ib, min(ib + block_size, size)):
                    for j in range(jb, min(jb + block_size, size)):
                        for k in range(kb, min(kb + block_size, size)):
                            c[i][k] += a[i][j] * b[j][k]


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

if __name__ == "__main__":
    m1= Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 1.xml").getMatriz()
    m2 = Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 2.xml").getMatriz()


    resultado = multiply2(m1, m2, int(len(m1) ** 0.5))
    imprimir_matriz(resultado)

