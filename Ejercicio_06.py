'''
Ejercicio 6. Función buscar_nombre :
Descripción del ejercicio:
Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
Caso de uso:
Incorpora los siguientes nombres a la lista y comprueba que la función
funciona correctamente: "Jaime", "Silvia" y "Ana".
'''

def encontrar_nombre (list_nombres):
  nombre_buscado = input("Introduce un nombre: ")
  if nombre_buscado in list_nombres:
    print(f"El nombre {nombre_buscado} Sí está en la lista")
    
  else:
    raise ValueError(f"El nombre {nombre_buscado} NO está en la lista")
    
lista_de_nombres =["Jaime", "Silvia", "Ana"]

encontrar_nombre(lista_de_nombres)