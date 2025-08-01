"""
Función que verifica si una cadena es un palindromo.
Un palindromo se lee igual de izquierda a derecha  que de
derecha a izquierda.

Args:
    inputStr(str): Cadena de texto a verificar.
    
Returns:
    bool: True si es palindromo, False si es lo contrario.
"""

def isPalindrome(inputStr):
    inputStr = inputStr.lower()
    return inputStr == inputStr[::-1]

print("-- Casos de Ejemplo --")

print("A)   isPalindrome('aabaa') :", isPalindrome("aabaa"))
print("B)   isPalindrome('abac') :", isPalindrome("abac"))
print("C)   isPalindrome('Salas') :", isPalindrome("Salas"))


