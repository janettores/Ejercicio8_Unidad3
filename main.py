from menu import menuOpciones
from claseLista import Lista
from claseObjectEncoder import ObjectEncoder


if __name__ == "__main__":
    listaAgentes = Lista()
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('personal.json')
    listaAgentes = jsonF.decodificarDiccionario(diccionario)

    menu = menuOpciones()
    menu.opciones(listaAgentes)