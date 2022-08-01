from re import T
from turtle import update
import configuracion
import palabras
import funciones
import os

#FEDERICO
def config():
    opc = 0
    op = 0
    band = True

    print("\t.:Menu Configuracion:.")
    print("\t¿Que quiere modificar.\n 1) Puntos.\n 2) Bonus.\n 3) Intentos.\n 4) Palabras.")
    while(band):
        try:
            opc = int(input("Opcion: "))
        except ValueError:
            print("Ingrese una de las opciones.")
        if(opc == 1):
            print("Los puntos de que nivel quiere modificar.")
            band2 = True
            band = False
            while(band2):

                #CAMBIO PUNTOS POR NIVEL
                nivelP = int(input("1) Nivel bajo. \n2) Nivel Medio. \n3) Nivel alto.\n"))
                if(nivelP == 1):
                    try:
                        puntos = (int(input("Cuantos puntos quiere poner: ")))
                        configuracion.nivelBajo.setPuntos(puntos)
                        print("Se agregaron los cambios.")
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                    
                elif(nivelP == 2):
                    try:
                        puntos = (int(input("Cuantos puntos quiere poner: ")))
                        configuracion.nivelMedio.setPuntos(puntos)
                        print("Se agregaron los cambios.")
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                elif(nivelP == 3):
                    try:
                        puntos = (int(input("Cuantos puntos quiere poner: ")))
                        configuracion.nivelAlto.setPuntos(puntos)
                        print("Se agregaron los cambios.")
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                else:
                    print("\tDijite una de las opciones mostradas.")

        # CAMBIO BONUS POR NIVEL
        elif(opc == 2):
            band = False
            print("Los Bonus de que nivel quiere modificar.")
            band2 = True
            while(band2):
                nivelB = int(input("1) Nivel bajo. \n2) Nivel Medio. \n3) Nivel alto.\n"))
                if(nivelB == 1):
                    try:
                        bonus = (int(input("Cuantos bonus quiere poner: ")))
                        configuracion.nivelBajo.setBonus(bonus)
                        print("Se agregaron los cambios.")
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                elif(nivelB == 2):
                    try:
                        bonus = (int(input("Cuantos bonus quiere poner: ")))
                        configuracion.nivelMedio.setBonus(bonus)
                        print("Se agregaron los cambios.")
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                elif(nivelB == 3):
                    try:
                        bonus = (int(input("Cuantos bonus quiere poner: ")))
                        configuracion.nivelAlto.setBonus(bonus)
                        print("Se agregaron los cambios.")
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                else:
                    print("\tDijite una de las opciones mostradas.")

        #CAMBIO INTENTOS POR NIVEL
        elif(opc == 3):
            band = False
            print("Los Intentos de que nivel quiere modificar.")
            band2 = True
            while(band2):
                nivelI = int(input("1) Nivel bajo. \n2) Nivel Medio. \n3) Nivel alto.\n"))
                if(nivelI == 1):
                    try:
                        intentos = (int(input("Cuantos intentos quiere poner: ")))
                        configuracion.nivelBajo.setIntentos(intentos)
                        band2 = False
                    except ValueError:
                        print("Escriba valores pedidos.")
                elif(nivelI == 2):
                        try:
                            intentos = (int(input("Cuantos intentos quiere poner: ")))
                            configuracion.nivelMedio.setIntentos(intentos)
                            band2 = False
                        except ValueError:
                            print("Escriba valores pedidos.")
                elif(nivelI == 3):
                        try:
                            intentos = (int(input("Cuantos intentos quiere poner: ")))
                            configuracion.nivelAlto.setIntentos(intentos)
                            band2 = False
                        except ValueError:
                            print("Escriba valores pedidos.")
                else:
                    print("\tDijite una de las opciones mostradas.")
        
        #MODIFICACION DE PALABRAS
        elif(opc == 4):
            band = False
            band2 = True
            print("\t¿Que desea realizar.\n 1) Agregar una nueva palabra.\n 2) Eliminar una nueva palabra.\n 3) Modificar una palabra ya esxistente.\n")
            while(band2):
                try:
                    op = int(input("Opcion: "))
                except ValueError:
                    print("Ingrese una de las opciones.") 
                if(op ==1):
                    try:
                        newpalabra = palabras.Palabra(input("Que palabra nueva desea ingresar: ").lower())
                        palabras.list.append(newpalabra)
                        print("Palabra añadida.")
                        band2 = False
                    except ValueError:
                        print("Ingrese una palabra valida y/o que no este en la lista.")
                elif(op == 2): 
                    deletepalabra = palabras.Palabra(input("¿Que palabra desea borrar: "))
                    for indi in list:
                        if(deletepalabra == indi):
                            palabras.list.pop(indi)
                            print("Palabra eleminiada")
                        else:
                            print("Revisar palabra, no se encuentra o no existe.")
                    band2 = False
                elif(op == 3):
                    modiPalabra = palabras.Palabra(input("Que palabra desea modificar: "))
                    for indi in list:
                        if(deletepalabra == indi):
                            palabras.list.append("modiPalabra")
                            print("Palabra modificada.")
                        else:
                            print("Revisar palabra, no se encuentra o no existe.")
                    band2 = False
                else:
                    print("Ingrese alguna de las opciones.")
        else:
            print("\tIngrese alguna de las opciones.")

def juego():
    cond = True
    bonus = True
    entrada = ""
    confNivel = 0
    palabraRespuesta = []
    nivel = funciones.verificarNivel()
    palabraAleatoria = funciones.obtenerPalabraRandom(nivel,palabras.list)
        
    for i in range(palabraAleatoria.getLongitud()):
        palabraRespuesta.append("*")
        
    confNivel = funciones.obtenerConfNivel(nivel)
    intentos = confNivel.getIntentos()
    puntos = confNivel.getPuntos()
    puntosBonus = confNivel.getBonus()
    
    while(intentos > 0):
        cond = True
        print("Intentos: ", intentos)
        print("Puntos: ", puntos+puntosBonus)
        print(*palabraRespuesta)
        entrada = input("Ingrese una letra o la palabra: ").lower()
        
        if (entrada == palabraAleatoria.getPalabra()) and bonus == True:
            print("acertaste a la primera!!")
            os.system("pause")
            intentos=0
        else:
            puntosBonus = 0
            bonus = False
            for sal,busq in enumerate(palabraAleatoria.getPalabra()):
                if(busq == entrada):
                    palabraRespuesta[sal] = entrada
                    cond = False
            
        if("".join(map(str,palabraRespuesta)) == palabraAleatoria.getPalabra()):
            print("Adivinaste la palabra!!!",palabraAleatoria.getPalabra())
            palabraAleatoria.setActivo(False)
            os.system("pause")
            intentos = 0
                
        #SOLUCION DE ERROR DE INTENTOS (MERA BOBADA)
        if(cond !=False):
            intentos = intentos - 1
        
        funciones.borrarPantalla()

#FUNCIONES CONFIGURACION:
#   1.CAMBIAR PUNTOS
#   1.CAMBIAR BONUS
#   1.CAMBIAR INTENTOS
#   1.AGREGAR, QUITAR Y EDITAR PALABRAS


#FUNCIONES JUEGO:
#   2.ESCOGER UNA PALABRA RANDOM DEPENDE DE LA DIFICULTAD
#   3.PINTAR PALABRA Y SUS PISTAS
#   4.SI ACERTO LA PALABRA DESACTIVARLA
#   5.SELECCIONAR LA COMPLEJIDAD
#   6.RESTAR INTENTOS