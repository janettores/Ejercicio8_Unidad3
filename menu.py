from claseInvestigador import Investigador
from claseDocente import Docente
from clasePersonalDeApoyo import PersonalApoyo
from claseDocenteInvestigador import DocenteInvestigador
from claseObjectEncoder import ObjectEncoder


class menuOpciones:
    __opcion: int

    def __init__(self):
        self.__opcion = 0

    def opciones(self, listaAgentes):
        while self.__opcion != 11:
            print("MENU DE OPCIONES")
            print("1) - Insertar a agentes a la colección.")
            print("2) - Agregar agentes a la colección.")
            print(
                "3) - Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
            print(
                "4) - Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
            print(
                "5) - Dada un área de investigación, contar la cantidad de agentes que son docente investigador, y la cantidad de investigadores que trabajen en ese área.")
            print(
                "6) - Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
            print(
                "7) - Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.")
            print("8) - Almacenar los datos de todos los agentes en el archivo “personal.json” ")
            print("9) - Tesorero: acceder a los gastos que la universidad tiene en concepto de sueldos.")
            print("10) - Abrir menu de opciones para Director.")
            print("11) - SALIR ")

            self.__opcion = int(input("Ingrese una opcion: "))

            if self.__opcion == 1:
                posicion = int(input("Ingrese la posicion en la que se va a insertar el agente: "))
                tipo = str(input(
                    "Ingrese el tipo de agente (docente, investigador, docente investigador, personal de apoyo): "))
                cuil = str(input("Ingrese el cuil del agente: "))
                apellido = str(input("Ingrese el apellido del agente: "))
                nombre = str(input("Ingrese el nombre del agente: "))
                sueldobasico = float(input("Ingrese el sueldo basico del agente: "))
                antiguedad = float(input("Ingrese la antiguedad del agente: "))

                if tipo == "docente":
                    carrera = str(input("Ingrese la carrera del docente: "))
                    cargo = str(input("Ingrese el cargo del docente: "))
                    catedra = str(input("Ingrese la catedra del docente: "))
                    agente = Docente(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
                    listaAgentes.insertarElemento(posicion, agente)

                elif tipo == "investigador":
                    areainvestigacion = str(input("Ingrese el area de investigacion del agente: "))
                    tipoinvestigacion = str(input("Ingrese el tipo de investigacion del agente: "))
                    agente = Investigador(cuil, apellido, nombre, sueldobasico, antiguedad, areainvestigacion,
                                          tipoinvestigacion)
                    listaAgentes.insertarElemento(posicion, agente)

                elif tipo == "docenteinvestigador" or tipo == "docente investigador":
                    carrera = str(input("Ingrese la carrera del docente: "))
                    cargo = str(input("Ingrese el cargo del docente: "))
                    catedra = str(input("Ingrese la catedra del docente: "))
                    areainvestigacion = str(input("Ingrese el area de investigacion del agente: "))
                    tipoinvestigacion = str(input("Ingrese el tipo de investigacion del agente: "))
                    categoriainvestigacion = int(input("Ingrese la categoria de investigacion: "))
                    importeextra = float(input("Ingrese el importe extra por docencia e investigacion: "))
                    agente = DocenteInvestigador(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo,
                                                 catedra, areainvestigacion, tipoinvestigacion, categoriainvestigacion,
                                                 importeextra)
                    listaAgentes.insertarElemento(posicion, agente)

                elif tipo == "personalapoyo" or tipo == "personal de apoyo":
                    categoria = str(input("Ingrese la categoria del personal de apoyo: "))
                    agente = PersonalApoyo(cuil, apellido, nombre, sueldobasico, antiguedad, categoria)
                    listaAgentes.insetrarElemento(posicion, agente)

                else:
                    print("Tipo ingresado de forma incorrecta")



            elif self.__opcion == 2:
                tipo = str(input(
                    "Ingrese el tipo de agente (docente, investigador, docente investigador, personal de apoyo): "))
                cuil = str(input("Ingrese el cuil del agente: "))
                apellido = str(input("Ingrese el apellido del agente: "))
                nombre = str(input("Ingrese el nombre del agente: "))
                sueldobasico = float(input("Ingrese el sueldo basico del agente: "))
                antiguedad = float(input("Ingrese la antiguedad del agente: "))

                if tipo == "docente":
                    carrera = str(input("Ingrese la carrera del docente: "))
                    cargo = str(input("Ingrese el cargo del docente: "))
                    catedra = str(input("Ingrese la catedra del docente: "))
                    agente = Docente(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
                    listaAgentes.agregarElemento(agente)

                elif tipo == "investigador":
                    areainvestigacion = str(input("Ingrese el area de investigacion del agente: "))
                    tipoinvestigacion = str(input("Ingrese el tipo de investigacion del agente: "))
                    agente = Investigador(cuil, apellido, nombre, sueldobasico, antiguedad, areainvestigacion,
                                          tipoinvestigacion)
                    listaAgentes.agregarElemento(agente)

                elif tipo == "docenteinvestigador" or tipo == "docente investigador":
                    carrera = str(input("Ingrese la carrera del docente: "))
                    cargo = str(input("Ingrese el cargo del docente: "))
                    catedra = str(input("Ingrese la catedra del docente: "))
                    areainvestigacion = str(input("Ingrese el area de investigacion del agente: "))
                    tipoinvestigacion = str(input("Ingrese el tipo de investigacion del agente: "))
                    categoriainvestigacion = str(input("Ingrese la categoria de investigacion: "))
                    importeextra = float(input("Ingrese el importe extra por docencia e investigacion: "))
                    agente = DocenteInvestigador(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo,
                                                 catedra, areainvestigacion, tipoinvestigacion, categoriainvestigacion,
                                                 importeextra)
                    listaAgentes.agregarElemento(agente)

                elif tipo == "personalapoyo" or tipo == "personal de apoyo":
                    categoria = str(input("Ingrese la categoria del personal de apoyo: "))
                    agente = PersonalApoyo(cuil, apellido, nombre, sueldobasico, antiguedad, categoria)
                    listaAgentes.agregarElemento(agente)

                else:
                    print("Tipo ingresado de forma incorrecta")

            elif self.__opcion == 3:
                posicion = int(input("Ingrese una posicion de la lista para mostrar que tipo de agente se encuentra: "))
                listaAgentes.mostrarElemento(posicion)

            elif self.__opcion == 4:
                ingcarrera = str(input("Ingrese el nombre de una carrera: "))
                listaAgentes.listadoDocentesInvestigadores(ingcarrera)

            elif self.__opcion == 5:
                ingareainvest = str(input("Ingrese un area de investigacion: "))
                listaAgentes.contarArea(ingareainvest)

            elif self.__opcion == 6:
                listaAgentes.listadoAgentes()


            elif self.__opcion == 7:
                ingcat = str(input("Ingrese una categoria de investigacion (I, II, III, IV o V): "))
                listaAgentes.listarSegunCategoria(ingcat)


            elif self.__opcion == 8:

                jsonF = ObjectEncoder()
                ldic = listaAgentes.toJSON()
                jsonF.guardarJSONArchivo(ldic, "test.json")
                listaAgentes.almacenarDatos()
                print("Se almaceno correctamente")

            elif self.__opcion == 9:

                print("INICIAR SESION")
                usuario = str(input("Ingrese el nombre de usuario: "))
                contrasena = str(input("Ingrese la contrasena: "))

                if usuario == "uTesorero" and contrasena == "ag@74ck":
                    ingdni = str(input("Ingrese el dni de un empleado: "))
                    band = listaAgentes.verificarDni(ingdni)
                    if band:
                        listaAgentes.gastosSueldoPorEmpleado(ingdni)
                    else:
                        print("El dni ingreasdo no corresponde a un")

                else:
                    print("El DNI ingresado no corresponde a ningun empleado registrado")

            elif self.__opcion == 10:

                print("INICIAR SESION")
                usuario = str(input("Ingrese el nombre de usuario: "))
                contrasena = str(input("Ingrese la contrasena: "))

                if usuario == "uDirector" and contrasena == "ufC77#!1":
                    print("MENU DE OPCIONES DE DIRECTOR: ")
                    oplocal = 0
                    while oplocal != 5:
                        print("1) - Modificar sueldo basico de un agente.")
                        print("2) - Modificar porcentaje por cargo de un docente.")
                        print("3) - Modificar porcentaje por categoria de personal de apoyo.")
                        print("4) - Modificar importe extra de docente investigador.")
                        print("5) - Salir.")
                        oplocal = int(input("Ingrese una opcion: "))
                        ingdni = str(input("Ingrese el dni de un empleado: "))

                        if oplocal == 1:

                            band = listaAgentes.verificarDni(ingdni)

                            if band == True:
                                nuevobasico = float(input("Ingrese el nuevo sueldo basico del agente: "))
                                listaAgentes.modificarBasico(ingdni, nuevobasico)
                            else:
                                print("El DNI ingresado no corresponde a ningun empleado registrado")

                        elif oplocal == 2:

                            band = listaAgentes.verificarDocente(ingdni)

                            if band == True:
                                nuevoPorcentaje = int(input("Ingrese el nuevo porcentaje: "))
                                listaAgentes.modificarPorcentajeporcargo(ingdni, nuevoPorcentaje)
                            else:
                                print("El DNI ingresado no corresponde a ningun Docente registrado.")


                        elif oplocal == 3:

                            band = listaAgentes.verificarPersonalDeApoyo(ingdni)

                            if band == True:
                                nuevoPorcentaje = int(input("Ingrese el nuevo porcentaje: "))
                                listaAgentes.modificarPorcentajeporcategoria(ingdni, nuevoPorcentaje)
                            else:
                                print("El DNI ingresado no corresponde a ningun Personal de Apoyo registrado.")

                        elif oplocal == 4:

                            band = listaAgentes.verificarDocenteInvestigador(ingdni)

                            if band == True:
                                nuevoImporteExtra = float(input("Ingrese el nuevo importe extra: "))
                                listaAgentes.modificarImporteExtra(ingdni, nuevoImporteExtra)
                            else:
                                print("El DNI ingresado no corresponde a ningun Docente Investigador registrado.")

                        else:
                            print("Salio del menu de director")

                else:
                    print("Usuario y/o contrasena incorrectos ")


            elif self.__opcion == 11:
                print("FIN DEL PROGRAMA")

            else:
                print("Opcion incorrecta, vuelva a ingresar una opcion \n")