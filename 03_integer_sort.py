"""
Función que ordena una lista de números enteros en orden ascendente
usando Bubble Sort, sin usar len() ni append().

Args:
    inputArray (list): Lista de números enteros a ordenar.
    
Returns: 
    list: Nueva lista con los elementos ordenados.
"""

def integerSort(inputArray):
    
    arr = []
    for elemento in inputArray:
        arr += [elemento] 
    
    
    n = 0
    for _ in arr:
        n += 1
    
    # Algoritmo Bubble Sort
    for i in range(n):
        hubo_intercambio = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                hubo_intercambio = True
                
        if not hubo_intercambio:
            break
        
    return arr



print("--- Casos de Ejemplo ---")
print(integerSort([10101, 0, -1, 4, 90, 2, 5])) 
print(integerSort([5, 3, 8, 4, 2]))             
print(integerSort([]))                          