'''
Ejercicio 3. Función encontrar_duplicado :
Descripción del ejercicio:
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
'''
lista_valores1 = [1, 6, 7, 6, 4, 9]
lista_valores2 = [1, 6, 7, 8, 4, 9]

def encontrar_duplicado (lista):
    valores = list()
    for valor in lista:
      if valor in valores:
         break
      else:
         valores.append(valor)
         
    
    if valores == None:
     print("No hay valores duplicados")

    else:
      print(f"El primer valor duplicado encontrado en la cadena es: {valores[-2]}")

primer_duplicado = encontrar_duplicado(lista_valores1)

primer_duplicado = encontrar_duplicado(lista_valores2)

