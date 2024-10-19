'''
Ejercicio 3. Función encontrar_duplicado :
Descripción del ejercicio:
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
'''
lista_valores = [1, 6, 7, 8, 4, 9]

def encontrar_duplicado (lista):
    valores = list()
    for valor in lista:
      if valor in valores:
         return (valor)
      else:
         valores.append(valor)

primer_duplicado = encontrar_duplicado(lista_valores)

if primer_duplicado == None:
   print("No hay valores duplicados")

else:
   print(f"El primer valor duplicado encontrado en la cadena es: {primer_duplicado}")