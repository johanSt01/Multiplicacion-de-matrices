import sys
import os
import time

# Agregar la ruta del paquete Persistencia al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Persistencia')))

# Importar la clase Persistencia
from Persistencia import Persistencia

def multiply6(a, b, blockSize):
    size = len(a)
    c = [[0.0] * size for _ in range(size)]

    for ib in range(0, size, blockSize):
        for jb in range(0, size, blockSize):
            for kb in range(0, size, blockSize):
                for i in range(ib, min(ib + blockSize, size)):
                    for j in range(jb, min(jb + blockSize, size)):
                        for k in range(kb, min(kb + blockSize, size)):
                            c[i][j] += a[i][k] * b[k][j]

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

    resultado = multiply6(m1, m2, int(len(m1) ** 0.5))
    imprimirMatriz(resultado)
