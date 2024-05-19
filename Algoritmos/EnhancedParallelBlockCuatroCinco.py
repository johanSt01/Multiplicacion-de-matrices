import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Agregar la ruta específica de Persistencia al PYTHONPATH
sys.path.append(r'C:\Users\Johan Stiven\Downloads\Algoritmos\Persistencia')

from Persistencia import Persistencia

def parallel_block_matrix_multiply(A, B, C, size, bsize):
    def calculate_partial_result(i1_start, i1_end):
        for i1 in range(i1_start, i1_end, bsize):
            for j1 in range(0, size, bsize):
                for k1 in range(0, size, bsize):
                    for i in range(i1, min(i1 + bsize, size)):
                        for j in range(j1, min(j1 + bsize, size)):
                            for k in range(k1, min(k1 + bsize, size)):
                                A[i][k] += B[i][j] * C[j][k]

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(calculate_partial_result, i1_start, i1_start + size // 2) for i1_start in [0, size // 2]]

        # Esperar a que todas las tareas se completen
        for future in as_completed(futures):
            future.result()

    return A

def imprimir_matriz(matriz):
    imprimir = ""
    for fila in matriz:
        for elemento in fila:
            imprimir += " " + str(elemento)
        imprimir += "\n"
    print(imprimir)

if __name__ == "__main__":
    m1= Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 1.xml").getMatriz()
    m2 = Persistencia.fromXML("Matrices de prueba/Caso 1/matriz 2.xml").getMatriz()
    m1l = len(m1)
    p = len(m2[0])
    m3 = [[0] * p for _ in range(m1l)]

    resultado = parallel_block_matrix_multiply(m3, m1, m2, m1l, 1)
    #imprimir_matriz(resultado)

    start_time_nano = time.time_ns()
    resultado = resultado = parallel_block_matrix_multiply(m3, m1, m2, m1l, 1)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano

    print(f"Tiempo que tarda el algoritmo Americano iterativo en ordenar el arreglo es: {elapsed_time_nano} nanosegundos")