
'''matrix = [[2, 4, 5, 8],
          [6, 3, 1, 9]]'''


#mostrar una matris no tan correcto

#print(matrix) #Llama a la matriz completa
#print(matrix[0]) #Llama a la primer posicion de esa matriz


#Mostrar una matris correctamente
'''
for i in range(len(matrix)):   #recorre filas
    for j in range(len(matrix[i])):  #recorre columnas
        print(matrix[i][j], end=" ")    #Llama de la lista i, el elemento j
    print("")
'''


#Como inicializarla
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial)->list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        
        matriz += [fila]
        
    return matriz

mi_matrix = inicializar_matriz(2, 4, 0)




'''def carga_matriz_secuencialmente(matriz:list):
    #Agregar las validaciones/retorno que sea necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input({f"Fila {i} Columna {j}: "}))
            
    carga_matriz_secuencialmente(mi_matrix)'''
