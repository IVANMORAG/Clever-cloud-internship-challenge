
# 🚀 Clever Cloud - Desafío Técnico Inicial

Este repositorio contiene las soluciones a los ejercicios de programación del desafío técnico inicial para la internship de Clever Cloud.

## 📋 Descripción del Desafío

El desafío consiste en resolver 3 problemas de programación fundamentales implementando algoritmos propios sin usar funciones nativas del lenguaje.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación principal
- **Git** - Control de versiones

## 📁 Estructura del Proyecto

```
clever-cloud-internship-challenge/
├── digits_sum.py           # Ejercicio 1: Suma de dígitos
├── palindrome_checker.py   # Ejercicio 2: Verificador de palíndromos  
├── integer_sort.py         # Ejercicio 3: Ordenamiento de enteros
└── README.md              # Este archivo
```

## 🎯 Ejercicios Implementados

### 1. Suma de Dígitos (`digits_sum.py`)
**Función:** `digitsSum(inputInt: int) -> int`

Calcula la suma de todos los dígitos de un número entero.

**Ejemplos:**
- `digitsSum(999)` → `27`
- `digitsSum(9184501)` → `28` 
- `digitsSum(12345)` → `15`

**Algoritmo:** Extracción de dígitos usando módulo y división entera.

### 2. Verificador de Palíndromos (`palindrome_checker.py`)
**Función:** `isPalindrome(inputStr: str) -> bool`

Verifica si una cadena de texto es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

**Ejemplos:**
- `isPalindrome("aabaa")` → `True`
- `isPalindrome("abac")` → `False`
- `isPalindrome("salas")` → `True`

**Algoritmo:** Comparación de caracteres desde los extremos hacia el centro.

### 3. Ordenamiento de Enteros (`integer_sort.py`)
**Función:** `integerSort(inputArray: List[int]) -> List[int]`

Ordena una lista de números enteros en orden ascendente sin modificar la lista original.

**Ejemplo:**
- `integerSort([5, -2, 10, 0, 3, -7])` → `[-7, -2, 0, 3, 5, 10]`

**Algoritmos implementados:**
- **Bubble Sort** (función principal)
- **Quick Sort** (función alternativa)

## 🚀 Cómo Ejecutar

### Prerrequisitos
- Python 3.x instalado en tu sistema

### Ejecución Individual
```bash
# Ejecutar cada ejercicio por separado
python digits_sum.py
python palindrome_checker.py
python integer_sort.py
```


## 🧪 Casos de Prueba

Cada archivo incluye casos de prueba específicos que validan:
- ✅ Casos de ejemplo proporcionados
- ✅ Casos edge (números negativos, arrays vacíos, strings vacíos)
- ✅ Casos con elementos duplicados
- ✅ Casos de un solo elemento

## 🎨 Características de la Implementación

### ✨ Principios Aplicados
- **No uso de funciones nativas** de ordenamiento o manipulación
- **Algoritmos implementados desde cero** para mostrar la lógica
- **Inmutabilidad** - Las funciones no modifican los datos originales
- **Claridad de código** con comentarios explicativos
- **Manejo de casos edge** para robustez

### 🔧 Algoritmos Utilizados
- **Extracción de dígitos:** Aritmética modular
- **Verificación de palíndromos:** Comparación bidireccional
- **Ordenamiento:** Bubble Sort y Quick Sort implementados manualmente


## 👨‍💻 Autor

Desarrollado como parte del proceso de selección para la internship de **Clever Cloud**.

## 📄 Licencia

Este proyecto es de uso educativo y está desarrollado específicamente para el desafío técnico de Clever Cloud.

---

⭐ **¡Gracias por revisar mi solución!** Si tienes alguna pregunta o sugerencia, no dudes en contactarme.