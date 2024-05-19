import sys
import os
import time
from lxml import etree as ET

# Agregar la ruta del paquete Persistencia al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Persistencia')))

# Importar la clase Persistencia
from Persistencia import Persistencia

# Agregar la ruta del paquete Algoritmos al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Algoritmos')))

# Importar las funciones desde EnhaEnhancedParallelBlockCuatroCincon.py
from EnhancedParallelBlockCuatroCinco import parallel_block_matrix_multiply, imprimir_matriz # type: ignore
from EnhancedParallelBlockTresCinco import parallel_block_matrix_multiply2, imprimir_matriz # type: ignore
from NaivLoopUnrollingFour import naivLoopUnrollingFour, imprimirMatriz # type: ignore
from NaivLoopUnrollinTwo import naivLoopUnrollingTwo, imprimirMatriz # type: ignore
from NaivOnArray import naive_on_array, imprimir_matriz # type: ignore
from ParallelBlockCincoCuatro import multiply, imprimir_matriz # type: ignore
from ParallelBlockCuatroCuatro import multiply2, imprimir_matriz # type: ignore
from ParallelBlockTresCuatro import multiply3, imprimir_matriz # type: ignore
from SequentialBlockCincoTres import multiply4, imprimir_matriz # type: ignore
from SequentialBlockCuatroTres import multiply5 # type: ignore
from SequentialBlockTresTres import multiply6 # type: ignore
from StrassenNaiv import StrassenNaiv # type: ignore
from StrassenWinograd import StrassenWinograd # type: ignore
from WinogradOriginal import winogradOriginal # type: ignore
from WinogradScaled import winogradScaled # type: ignore


def main():
    m1 = Persistencia.fromXML("Matrices de prueba/Caso 7/matriz 1.xml").getMatriz()
    m2 = Persistencia.fromXML("Matrices de prueba/Caso 7/matriz 2.xml").getMatriz()
    m1l = len(m1)
    m2l = len(m2)
    p = len(m2[0])
    m3 = [[0] * p for _ in range(m1l)]
    m4 = [[0 for _ in range(m2l)] for _ in range(m1l)]
    m5 = [[0.0] * m2l for _ in range(m1l)]


    # punto 1
    start_time_nano = time.time_ns()
    resultado = parallel_block_matrix_multiply(m3, m1, m2, m1l, 1)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear el elemento raíz del XML
    root = ET.Element("persistencia")

    # Crear elemento para los tiempos de ejecución
    tiempos_elem = ET.SubElement(root, "tiempos")

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "IV-V EnhancedParallelBlock"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo EnhancedParallelBlockCuatroCinco es: {elapsed_time_nano} nanosegundos")

    # punto 2
    start_time_nano = time.time_ns()
    resultado = parallel_block_matrix_multiply2(m3, m1, m2, m1l, 1)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "III-V EnhancedParallelBlock"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo EnhancedParallelBlockTresCinco es: {elapsed_time_nano} nanosegundos")

    # punto 3
    start_time_nano = time.time_ns()
    resultado = naivLoopUnrollingFour(m1, m2, m4, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimirMatriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "NaivLoopUnrollingFour"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo NaivLoopUnrollingFour es: {elapsed_time_nano} nanosegundos")

    # punto 4
    start_time_nano = time.time_ns()
    resultado = naivLoopUnrollingTwo(m1, m2, m4, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimirMatriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "NaivLoopUnrollinTwo"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo naivLoopUnrollingTwo es: {elapsed_time_nano} nanosegundos")

    # punto 5
    start_time_nano = time.time_ns()
    resultado = naive_on_array(m1, m2, m4, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimirMatriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "NaivOnArray"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo NaivOnArray es: {elapsed_time_nano} nanosegundos")

    # punto 6
    start_time_nano = time.time_ns()
    resultado = multiply(m1, m2, int(len(m1) ** 0.5))
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "ParallelBlockCincoCuatro"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo ParallelBlockCincoCuatro es: {elapsed_time_nano} nanosegundos")

    # punto 7
    start_time_nano = time.time_ns()
    resultado = multiply2(m1, m2, int(len(m1) ** 0.5))
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "ParallelBlockCuatroCuatro"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo ParallelBlockCuatroCuatro es: {elapsed_time_nano} nanosegundos")

    # punto 8
    start_time_nano = time.time_ns()
    resultado = multiply3(m1, m2, int(len(m1) ** 0.5))
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "ParallelBlockTresCuatro"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo ParallelBlockTresCuatro es: {elapsed_time_nano} nanosegundos")

    # punto 9
    start_time_nano = time.time_ns()
    resultado = multiply4(m1, m2, int(len(m1) ** 0.5))
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "SequentialBlockCincoTres"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo SequentialBlockCincoTres es: {elapsed_time_nano} nanosegundos")

    # punto 10
    start_time_nano = time.time_ns()
    resultado = multiply5(m1, m2, int(len(m1) ** 0.5))
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "SequentialBlockCuatroTres"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo SequentialBlockCuatroTres es: {elapsed_time_nano} nanosegundos")

    # punto 11
    start_time_nano = time.time_ns()
    resultado = multiply6(m1, m2, int(len(m1) ** 0.5))
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "SequentialBlockTresTres"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo SequentialBlockTresTres es: {elapsed_time_nano} nanosegundos")

    # punto 12
    strassenNaiv = StrassenNaiv()
    start_time_nano = time.time_ns()
    resultado = strassenNaiv.strassenNaiv(m1, m2, m5, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "StrassenNaiv"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo StrassenNaiv es: {elapsed_time_nano} nanosegundos")

    # punto 13
    strassenWinograd = StrassenWinograd()
    start_time_nano = time.time_ns()
    resultado = strassenWinograd.strassenWinograd(m1, m2, m5, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "StrassenWinograd"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo StrassenWinograd es: {elapsed_time_nano} nanosegundos")

    # punto 14
    start_time_nano = time.time_ns()
    resultado = winogradOriginal(m1, m2, m5, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "WinogradOriginal"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo WinogradOriginal es: {elapsed_time_nano} nanosegundos")

    # punto 15
    start_time_nano = time.time_ns()
    resultado = winogradScaled(m1, m2, m5, m1l, m2l, p)
    end_time_nano = time.time_ns()
    elapsed_time_nano = end_time_nano - start_time_nano
    #imprimir_matriz(resultado)

    # Crear entrada para el tiempo de ejecución
    entry_elem = ET.SubElement(tiempos_elem, "entry")
    key_elem = ET.SubElement(entry_elem, "key")
    key_elem.text = "WinogradScaled"
    value_elem = ET.SubElement(entry_elem, "value")
    value_elem.text = str(elapsed_time_nano)

    print(f"Tiempo que tarda el algoritmo WinogradScaled es: {elapsed_time_nano} nanosegundos")


    # Crear el árbol XML
    tree = ET.ElementTree(root)

    # Guardar el árbol XML en un archivo
    ruta = "Tiempos de ejecucion python/Tiempos-Caso 7.xml"
    with open(ruta, "wb") as f:
        tree.write(f, pretty_print=True, xml_declaration=True, encoding="utf-8")


if __name__ == "__main__":
    main()
