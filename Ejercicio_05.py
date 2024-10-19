'''
Ejercicio 5. Función es_anagrama :
Descripción del ejercicio:
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
'''

def es_anagrama (palabra1, palabra2):

  return (print("Son anagrama") if sorted(palabra1.lower()) == sorted(palabra2.lower()) else print("No es anagrama"))
  
palabra1 = "juan"
palabra2 = "janu"

es_anagrama(palabra1, palabra2)

palabra1 = "juan"
palabra2 = "jalu"

es_anagrama(palabra1, palabra2)