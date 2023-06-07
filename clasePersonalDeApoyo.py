from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria: int

    def __init__(self, cuil='', apellido='', nombre='', sueldobasico=0, antiguedad=0, categoria=0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categoria = categoria
        self.__extraporcategoria = self.calcularExtraPorCategoria()

    def calcularExtraPorCategoria(self):

        if self.__categoria >= 1 and self.__categoria <= 10:
            extraporcategoria = (10 / 100)

        elif self.__categoria >= 11 and self.__categoria <= 20:
            extraporcategoria = (20 / 100)

        elif self.__categoria >= 21 and self.__categoria <= 22:
            extraporcategoria = (30 / 100)

        return extraporcategoria

    def getCategoria(self):
        return self.__categoria

    def getSueldo(self):
        sueldotot = super().getSueldoBasico() + (super().getSueldoBasico() * (super().getAntiguedad() / 100)) + (
                    super().getSueldoBasico() * self.__extraporcategoria)

        return sueldotot

    def cambiarPorcentaje(self, nuevoPorcentaje):
        print("El sueldo antes de cambiar el porcentaje es: {}".format(self.getSueldo()))
        self.__extraporcategoria = nuevoPorcentaje / 100
        print("El sueldo con el nuevo porcentaje es: {}".format(self.getSueldo()))

    def __str__(self):
        return super().__str__() + "\nCategoria: " + str(self.__categoria)