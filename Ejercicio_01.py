'''
Ejercicio 1. Función contar_caracteres :
Descripción del ejercicio:
Crea una función que cuente el número de caracteres en una cadena de texto dada.
'''

def contar_caracteres (cadena_texto):
    return (len(cadena_texto))

cadena = input("Introduce una cadena de texto: ")

print(f"El número de caracteres de la cadena es de {contar_caracteres(cadena)}")

