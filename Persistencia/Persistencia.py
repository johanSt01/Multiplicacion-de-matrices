from lxml import etree
import os

class Persistencia:
    def __init__(self, matriz=None):
        self.matriz = matriz

    def getMatriz(self):
        return self.matriz

    def setMatriz(self, matriz):
        self.matriz = matriz

    def toXML(self, filePath):
        root = etree.Element("Persistencia")
        for fila in self.matriz:
            matriz_elem = etree.SubElement(root, "matriz")
            for valor in fila:
                etree.SubElement(matriz_elem, "item").text = str(valor)

        tree = etree.ElementTree(root)
        with open(filePath, "wb") as file:
            tree.write(file, pretty_print=True)

    @staticmethod
    def fromXML(filePath):
        if not os.path.exists(filePath):
            print(f"Error: el archivo {filePath} no existe.")
            return None
        try:
            tree = etree.parse(filePath)
            matriz = []
            for matriz_elem in tree.xpath("//matriz"):
                fila = [int(item_elem.text) for item_elem in matriz_elem.xpath("./item")]
                matriz.append(fila)
            return Persistencia(matriz)
        except Exception as e:
            print(f"Error inesperado al procesar el archivo {filePath}: {e}")
            return None

    @staticmethod
    def imprimirMatriz(matriz):
        for fila in matriz:
            print(fila)

    @staticmethod
    def main():
        #Prueba-ejemplo de escritura y lectura de matrices
        try:
            matriz = [[2, 4], [1, 3]]
            persistentArray = Persistencia(matriz)
            #persistentArray.toXML("Matrices de prueba/Caso 1/de pruebaPY.xml")

            filePath = "Matrices de prueba/Caso 2/matriz 1.xml"
            print(f"Intentando cargar la matriz desde {filePath}")
            newArray = Persistencia.fromXML(filePath)
            if newArray and newArray.getMatriz():
                loadedM = newArray.getMatriz()
                Persistencia.imprimirMatriz(loadedM)
            else:
                print("Error al cargar la matriz desde el archivo XML.")
        except Exception as e:
            print("Error inesperado en main:", e)

if __name__ == "__main__":
    Persistencia.main()