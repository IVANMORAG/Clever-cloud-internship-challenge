"""
Función que calcula la suma de todos los dígitos de un número 
entero.

Args:
    inputInt (int): Número entero del cual calcular la suma de 
    dígitos.
    
Returns:
    int: Suma de todos los dígitos.
"""

def digitsSum(inputInt):
    num = abs(inputInt)
    suma = 0
    
    if num == 0:
        return 0
    
    while num > 0:
        digito = num % 10
        suma = suma + digito
        num = num // 10
        
    return suma


print("--- Casos de Ejemplo ---")
print("A)   digitsSum(999): ", (digitsSum(999)))
print("B)   digitsSum(9184501): ", (digitsSum(9184501)))
print("C)   digitsSum(12345): ", (digitsSum(12345)))