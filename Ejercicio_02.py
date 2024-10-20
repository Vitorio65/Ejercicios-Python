'''
Ejercicio 2. Función calcular_promedio :
Descripción del ejercicio:
Crea una función que calcule el promedio de una lista de números.
'''
lista_números = [1, 6, 6, 4, 9,"a"]

def promedio (lista):
    try:
       suma = sum (num for num in lista)
       return(suma / len(lista))
    except TypeError:
       return("No se puede hallar la medida de la lista") 
   
print(promedio(lista_números))