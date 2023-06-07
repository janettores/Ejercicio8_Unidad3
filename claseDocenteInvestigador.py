from claseDocente import Docente
from claseInvestigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categoria: str
    __extra: float

    def __init__(self, cuil='', apellido='', nombre='', sueldobasico=0, antiguedad=0, carrera='', cargo='', catedra='',
                 areainvestigacion='', tipoinvestigacion='', categoriainvestigacion='', importeextra=0):
        Docente.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, areainvestigacion,
                              tipoinvestigacion)
        self.__categoria = categoriainvestigacion
        self.__extra = importeextra

    def getCategoria(self):
        return self.__categoria

    def getExtra(self):
        return self.__extra

    def getSueldo(self):
        sueldoDocente = super(Docente, self).getSueldo()
        sueldotot = sueldoDocente + self.__extra

        return sueldotot

    def cambiarImporteExtra(self, nuevoExtra):
        self.__extra = nuevoExtra
        print("Se modifico el importe extra que recibe el docente investigador.")

    def __str__(self):
        return super().__str__() + "\n Categoria: " + self.__categoria + " Importe extra por docencia e investigacion: $" + str(
            self.__extra)

    def __lt__(self, otro):
        return super().getNombre() < otro.getNombre()