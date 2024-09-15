import random
import os
import time
import re

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"
BOLD = "\033[1m"
REG = "\033[0m"




def default():
    tablero = [["1","2","3"],["4","5","6"],["7","8","9"]]
    return tablero

turno = 0
tablero = default()

def imprimirTablero(tablero):
    os.system("cls")
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(filas):
        print()
        for j in range (columnas):
            if tablero[i][j] == "X":
                print(f" |{BLUE}{BOLD}{tablero[i][j]}{REG}" "|", end="")
            elif tablero[i][j] == "O":
                print(f" |{PURPLE}{BOLD}{tablero[i][j]}{REG}" "|", end="")
            else:    
                print(f" |{tablero[i][j]}" "|", end="")


def marcar(tablero):
    pos = int(input("\ningrese posicion para marcar: "))
    condicion = not True

    for i in range(1,4):
        if pos == i:
            if "X" in tablero[0][i-1] or "O" in tablero[0][i-1]:
                print(f"{RED}el casillero ya se encuentra marcado!{REG}")
                time.sleep(1)
            else:
                tablero[0][i-1] = "X"

    for i in range(4,7):
            if pos == i:
                if "X" in tablero[1][i-4] or "O" in tablero[1][i-4]:
                    print(f"{RED}el casillero ya se encuentra marcado!{REG}")
                    time.sleep(1)
                else:
                    tablero[1][i-4] = "X"

    for i in range(7,10):
            if pos == i:
                if "X" in tablero[2][i-7] or "O" in tablero[2][i-7]:
                    print(f"{RED}el casillero ya se encuentra marcado!{REG}")
                    time.sleep(1)
                else:
                    tablero[2][i-7] = "X"
    return tablero


def tateti(marcado):
    usuario = 0
    maquina = 0
    filas= 3

    for i in range(filas):
        if marcado[i][0] == marcado[i][1] and marcado[i][1] == marcado[i][2]:
            if marcado[i][0] == "O":
                maquina = 1
            elif marcado[i][0] == "X":
                usuario = 1
        elif marcado[0][i] == marcado[1][i] and marcado[1][i] == marcado[2][i]:
            if marcado[0][i] == "O":
                maquina = 1
            elif marcado[0][i] == "X":
                usuario = 1
    
    if marcado[0][0] == marcado[1][1] and marcado[1][1] == marcado[2][2]:
        if marcado[0][0] == "O":
                maquina = 1
        elif marcado[0][0] == "X":
                usuario = 1
    elif marcado[0][2] == marcado[1][1] and marcado[1][1] == marcado[2][0]:
        if marcado[0][2] == "O":
                maquina = 1
        elif marcado[0][2] == "X":
                usuario = 1

    if maquina == 1:
        print()
        print(f"{GREEN}{BOLD}\nTA-TE-TI - Perdiste loser!!{REG}")
        return True
    if usuario == 1:
        print()
        print(f"{GREEN}{BOLD}\nTA-TE-TI - Ganaste, sos crack!{REG}")
        return True
    else:
        return False
    
def turnoMaquina(tablero):
    pos = random.randint(1,9)
    for i in range(1,4):
        if pos == i:
            if "X" in tablero[0][i-1] or "O" in tablero[0][i-1]:
                turnoMaquina(tablero)
            else:
                print(f"\nturno de la maquina: {i}")
                tablero[0][i-1] = "O"

    for i in range(4,7):
            if pos == i:
                if "X" in tablero[1][i-4] or "O" in tablero[1][i-4]:
                    turnoMaquina(tablero)
                else:
                    print(f"\nturno de la maquina: {i}")
                    tablero[1][i-4] = "O"

    for i in range(7,10):
            if pos == i:
                if "X" in tablero[2][i-7] or "O" in tablero[2][i-7]:
                    turnoMaquina(tablero)
                else:
                    print(f"\nturno de la maquina: {i}")
                    tablero[2][i-7] = "O"

    return tablero

def jugar(turno):
    condicion = not True
    estado = tateti(tablero)

    if condicion == estado:
        if turno !=9:
            tab = marcar(tablero)
            imprimirTablero(tab)
            turno+=1
        else:
            print(f"{GREEN}{BOLD}\nempate{REG}") 
    estado = tateti(tablero)
    
    if condicion == estado:
        if turno !=9:
            tab = turnoMaquina(tablero)
            imprimirTablero(tab)
            turno+=1
            jugar(turno)
        else:
            print(f"{GREEN}{BOLD}\nempate{REG}")    
    
    if condicion != estado:
         again = int(input("jugar de nuevo? 1: si - 2: no: "))
         if again == 1:
              iniciar()
         else:
            quit()
            

def iniciar():
    global tablero, turno
    tablero = default()
    turno = 0
    imprimirTablero(tablero)
    jugar(turno)

iniciar()



















