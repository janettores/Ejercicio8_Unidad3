from zope.interface import implementer

from interfaceR import IAgente
from claseNodo import Nodo

from InterfaceDirector import IDirector
from InterfaceTesorero import ITesorero

@implementer(IAgente)
@implementer(IDirector)
@implementer(ITesorero)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int

    def __init__(self):
        self.__comienzo: Nodo
        self.__actual: Nodo
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, agente):
        nodo = Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def listarDatosVehiculos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def insertarElemento(self, posicion, agente):
        nuevo = Nodo(agente)
        if self.__comienzo == None:
            nuevo.setSiguiente(self.__comienzo)
        elif (self.__indice == posicion):
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        else:
            p = self.__comienzo
            anterior = self.__comienzo
            while (p != None) and (posicion > self.__indice):
                anterior = p
                p = p.getSiguiente()
                self.__indice += 1
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(p)

    def mostrarElemento(self, posicion):
        aux = self.__comienzo
        while aux != None and self.__indice != posicion:
            aux = aux.getSiguiente()
            self.__indice += 1

        if self.__indice == posicion:
            aux.getTipo()
        else:
            print("Posicion no existe")

    def listadoDocentesInvestigadores(self, ingcarrera):
        aux = self.__comienzo
        listaordenada = []
        while aux != None:
            if (aux.getDatoCarrera() == ingcarrera):
                listaordenada.append(aux.getDato())
            aux = aux.getSiguiente()

        listaordenada.sort()
        for docenteinvestigador in listaordenada:
            print(docenteinvestigador)

    def contarArea(self, area):
        aux = self.__comienzo
        contDocenteInvestigador = 0
        contInvestigador = 0
        while aux != None:
            if (aux.getDatoArea() == area):
                if (aux.esDocInvestigador()):
                    contDocenteInvestigador += 1
                elif (aux.esInvestigador()):
                    contInvestigador += 1
            aux = aux.getSiguiente()

        print("El area de investigacion {} tiene {} docente/s investigador/es, y {} investigador/es".format(area,
                                                                                                            contDocenteInvestigador,
                                                                                                            contInvestigador))

    def listadoAgentes(self):
        aux = self.__comienzo
        listaAgentes = []

        while aux != None:
            agente = aux.getAgente()
            listaAgentes.append(agente)
            aux = aux.getSiguiente()

        listaAgentes.sort()

        for agente in listaAgentes:
            print(agente)

    def listarSegunCategoria(self, ingcat):
        importeSecretaria = 0
        aux = self.__comienzo

        while aux != None:
            if aux.esDocInvestigador():
                if aux.getDatoCategoria() == ingcat:
                    aux.mostrarDocInvestigador()
                    importeSecretaria += aux.getDatoImporteExtra()
            aux = aux.getSiguiente()
        print("El importe total que debe solicitar la Secreteria de Investigacion al Ministerio es: {}".format(
            importeSecretaria))

    def toJSON(self):
        aux = self.__comienzo
        ld = []
        while aux != None:
            vdic = aux.toJSON()
            ld.append(vdic)
            aux = aux.getSiguiente()

        return ld

    def verificarDni(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni:
                band = True
            aux = aux.getSiguiente()

        return band

    def gastosSueldoPorEmpleado(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni:
                band = True
                print("El sueldo del empleado ingresado es: {}".format(aux.getDatoSueldo()))
            aux = aux.getSiguiente()

    def modificarBasico(self, ingdni, nuevobasico):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni:
                band = True
                aux.modificarSueldoBasico(nuevobasico)
            aux = aux.getSiguiente()

    def verificarDocente(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocente() == True:
                band = True
            aux = aux.getSiguiente()

        return band

    def modificarPorcentajeporcargo(self, ingdni, nuevoPorcentaje):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocente() == True:
                band = True
                aux.modificarPorcentaje(nuevoPorcentaje)
            aux = aux.getSiguiente()

    def verificarPersonalDeApoyo(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esPersonalDeApoyo() == True:
                band = True
            aux = aux.getSiguiente()
        return band

    def modificarPorcentajeporcategoria(self, ingdni, nuevoPorcentaje):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esPersonalDeApoyo() == True:
                band = True
                aux.modificarPorcentaje(nuevoPorcentaje)
            aux = aux.getSiguiente()

    def verificarDocenteInvestigador(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocInvestigador() == True:
                band = True
            aux = aux.getSiguiente()

        return band

    def modificarImporteExtra(self, ingdni, nuevoImporteExtra):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocInvestigador() == True:
                band == True
                aux.modificarExtra(nuevoImporteExtra)
            aux = aux.getSiguiente()