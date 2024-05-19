import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

def parallel_block_matrix_multiply2(A, B, C, size, bsize):
    # Función para multiplicar un bloque de matrices
    def multiply_block(i_start, i_end):
        for i1 in range(i_start, i_end):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                A[i][j] += B[i][k] * C[k][j]

    # Dividir la tarea de multiplicación en dos partes
    middle_row = size // 2

    # Crear ThreadPoolExecutor para administrar hilos
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Primer hilo para la primera mitad de las filas
        future1 = executor.submit(multiply_block, 0, middle_row)
        # Segundo hilo para la segunda mitad de las filas
        future2 = executor.submit(multiply_block, middle_row, size)

        # Esperar a que ambos hilos terminen
        for future in as_completed([future1, future2]):
            future.result()

    return A

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

if __name__ == "__main__":
    m1= Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 1.xml").getMatriz()
    m2 = Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 2.xml").getMatriz()
    m1l = len(m1)
    m2l = len(m2)
    p = len(m2[0])
    m3 = [[0] * p for _ in range(m1l)]
    resultado = parallel_block_matrix_multiply2(m3, m1, m2, len(m1), 1)
    imprimir_matriz(resultado)