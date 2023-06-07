from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from clasePersonalDeApoyo import PersonalApoyo
from claseInvestigador import Investigador


class Nodo:
    __agente: object
    __siguiente: object

    def __init__(self, agente):
        self.__agente = agente
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__agente

    def toJSON(self):
        pass

    def getTipo(self):

        if isinstance(self.__agente, Docente):
            print("Docente")
        elif isinstance(self.__agente, DocenteInvestigador):
            print("Docente Investigador")
        elif isinstance(self.__agente, PersonalApoyo):
            print("Personal de apoyo")
        elif isinstance(self.__agente, Investigador):
            print("Investigador")

    def getDatoCarrera(self):
        if isinstance(self.__agente, Docente) or isinstance(self.__agente, DocenteInvestigador):
            return self.__agente.getCarrera()
        else:
            return False

    def getDatoArea(self):
        if isinstance(self.__agente, DocenteInvestigador) or isinstance(self.__agente, Investigador):
            return self.__agente.getArea()
        else:
            return False

    def esInvestigador(self):
        return isinstance(self.__agente, Investigador)

    def esDocInvestigador(self):
        return isinstance(self.__agente, DocenteInvestigador)

    def esDocente(self):
        return isinstance(self.__agente, Docente)

    def esPersonalDeApoyo(self):
        return isinstance(self.__agente, PersonalApoyo)

    def getAgente(self):
        cadena = self.__agente.getNombre() + " " + self.__agente.getApellido() + " "
        if isinstance(self.__agente, DocenteInvestigador):
            cadena += "Docente Investigador $"
        elif isinstance(self.__agente, Docente):
            cadena += "Docente $"
        elif isinstance(self.__agente, Investigador):
            cadena += "Investigador $"
        elif isinstance(self.__agente, PersonalApoyo):
            cadena += "Personal de Apoyo $"

        cadena += str(self.__agente.getSueldo())

        return cadena

    def getDatoCategoria(self):
        return self.__agente.getCategoria()

    def mostrarDocInvestigador(self):
        print("{} {} \tImporte Extra por docencia e investigacion: {}".format(self.__agente.getApellido(),
                                                                              self.__agente.getNombre(),
                                                                              self.__agente.getExtra()))

    def getDatoImporteExtra(self):
        return self.__agente.getExtra()

    def toJSON(self):
        if isinstance(self.__agente, DocenteInvestigador):
            d = dict(tipo="docenteinvestigador", cuil=self.__agente.getCuil(), apellido=self.__agente.getApellido(),
                     nombre=self.__agente.getNombre(), sueldobasico=self.__agente.getSueldoBasico(),
                     antiguedad=self.__agente.getAntiguedad(), carrera=self.__agente.getCarrera(),
                     cargo=self.__agente.getCargo(), catedra=self.__agente.getCatedra(),
                     areainvestigacion=self.__agente.getArea(), tipoinvestigacion=self.__agente.getTipo(),
                     categoria=self.__agente.getCategoria(), importeextra=self.__agente.getExtra())
        elif isinstance(self.__agente, Docente):
            d = dict(tipo="docente", cuil=self.__agente.getCuil(), apellido=self.__agente.getApellido(),
                     nombre=self.__agente.getNombre(), sueldobasico=self.__agente.getSueldoBasico(),
                     antiguedad=self.__agente.getAntiguedad(), carrera=self.__agente.getCarrera(),
                     cargo=self.__agente.getCargo(), catedra=self.__agente.getCatedra())
        elif isinstance(self.__agente, Investigador):
            d = dict(tipo="investigador", cuil=self.__agente.getCuil(), apellido=self.__agente.getApellido(),
                     nombre=self.__agente.getNombre(), sueldobasico=self.__agente.getSueldoBasico(),
                     antiguedad=self.__agente.getAntiguedad(), areainvestigacion=self.__agente.getArea(),
                     tipoinvestigacion=self.__agente.getTipo())
        elif isinstance(self.__agente, PersonalApoyo):
            d = dict(tipo="personalapoyo", cuil=self.__agente.getCuil(), apellido=self.__agente.getApellido(),
                     nombre=self.__agente.getNombre(), sueldobasico=self.__agente.getSueldoBasico(),
                     antiguedad=self.__agente.getAntiguedad(), categoria=self.__agente.getCategoria())
        return d

    def getDatoDni(self):
        return self.__agente.getDni()

    def getDatoSueldo(self):
        return self.__agente.getSueldo()

    def modificarSueldoBasico(self, nuevobasico):
        self.__agente.cambiarSueldoBasico(nuevobasico)

    def modificarPorcentaje(self, nuevoporcentaje):
        self.__agente.cambiarPorcentaje(nuevoporcentaje)

    def modificarExtra(self, nuevoImporteExtra):
        self.__agente.cambiarImporteExtra(nuevoImporteExtra)