'''
desarrollar un tablero que represente de batalla naval:
tiene un tablero, barcos

ejemplo:
Batalla Naval
=============

Columnas
0   1   2   3   4        (5x5)
0 | 0 | 0 | 0 | 0 |  0   F
0 | 0 | 0 | 0 | 0 |  1   I
0 | 0 | 0 | 0 | 0 |  2   L
0 | 0 | 0 | 0 | 0 |  3   A
0 | 0 | 0 | 0 | 0 |  4   S

Hacer una inicializacion de 5x5 con valor 0
'''


'''
import random


mi_matriz = inicializar_matriz(5, 5, 0)
print(mi_matriz)

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicia:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicia] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" | ")
        print("")

def posicionar_barcos(tablero, cant_barcos):
    fila = random.randit(0, len(tablero) - 1)
    col = random.randit(0, len(tablero) - 1)
    for i in range(cant_barcos):
        tablero[fila][col] = "B"
        
cant_barcos = int(input("Ingrese la cantidad de barcos: "))
tablero = inicializar_matriz(5, 5, 0)
posicionar_barcos(tablero, cant_barcos)
imprimir_tablero(tablero)
'''

import random

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial: any) ->list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def imprimir_tablero(tablero) ->list:
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" | ")
        print('')
    return ""

def carga_tablero(tablero, can_barcos):
    
    for i in range(can_barcos):
        filas = random.randint(0, len(tablero) - 1)
        columnas = random.randint(0, len(tablero) - 1)
        tablero [filas][columnas] = "B"

def batalla(tablero, cantidad_intentos):
    for i in range(cantidad_intentos):
        fila = int(input("Fila: "))
        columna = int(input("Columna: "))
        
        if tablero[fila][columna] == "B":
            print("HUNDIDO")
            tablero [fila][columna] = "X"
            
        else:
            print("AGUA")
            tablero[fila][columna] = "F"
    
    
tablero = inicializar_matriz(5, 5, 0)
cantidad_barcos = int(input("Ingrese la cantidad de barcos: "))
cantidad_intentos = 5

carga_tablero(tablero, cantidad_barcos)
batalla (tablero, cantidad_intentos)
imprimir_tablero(tablero)