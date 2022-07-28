import random
import configuracion
import os

def verificarNivel():
    cond = True
    while(cond):
            try:
                nivel = int(input("Que nivel desea\n\t1. Bajo\n\t2. Medio\n\t3. Alto"))
            except ValueError:
                print("Ingrese el número que acompaña a la letra por favor")
            else:
                if(nivel == 1 or nivel == 2 or nivel == 3):
                    cond = False
                    return nivel
                else:
                    print("Ingrese una opción valida")

def obtenerPalabraRandom(nivel,listaPalabras):
    cond = True
    while(cond):
        palabraAleatoria = random.choice(listaPalabras)
        if(nivel == 1):
            if(palabraAleatoria.getLongitud()<=5 and palabraAleatoria.getActivo()==True):
                cond = False
                return palabraAleatoria
        elif(nivel == 2):
            if(palabraAleatoria.getLongitud() >5 and palabraAleatoria.getLongitud()<=12 and palabraAleatoria.getActivo()==True):
                cond = False
                return palabraAleatoria
        elif(nivel == 3):
            if(palabraAleatoria.getLongitud()>12 and palabraAleatoria.getActivo()==True):
                cond=False
                return palabraAleatoria   
        
def obtenerConfNivel(nivel):
    if nivel == 1:
        return configuracion.nivelBajo
    elif nivel == 2:
        return configuracion.nivelMedio
    else:
        return configuracion.nivelAlto
    
def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
