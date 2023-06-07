from zope.interface import Interface

class IAgente(Interface):

    def insertarElemento(posicion):
        pass

    def agregarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass
