'''
Ejercicio 16. Función procesar_texto :
Explicación del ejercicio:
Descripción:
Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
  contar_palabras , reemplazar_palabras , eliminar_palabra.
  Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.
Código a seguir:
  1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
  2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
  3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
  4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
Caso de uso:
  texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
  Dado el texto de ejemplo, llama a la función procesar_texto para probar sus funcionalidades:
  Cuenta el número de veces que aparece cada palabra.
  Reemplaza la palabra texto por relato.
  Elimina la palabra ejemplo.
'''

def contar_palabras(texto):
  texto = texto.lower()
  palabras = texto.split()
  contador = {}
  for palabra in palabras:
      if palabra in contador:
         contador[palabra] += 1
      else:
          contador[palabra] = 1
    
  return (contador)
  
  
def reemplazar_palabras(texto, palabra_original, palabra_nueva): 
  try:
    texto = texto.replace(palabra_original, palabra_nueva)
    return(texto)
  except Exception as e:
    print(f"No se ha podido convertir {e} \n")
    
def eliminar_palabra(texto, palabra_eliminar): 
  try:
    texto = texto.replace(palabra_eliminar, "")
    return(texto)
  except Exception as e:
    print(f"No se ha podido convertir {e} \n")
    
def procesar_texto(opción, *args):
  if opción == "contar":
    contador = contar_palabras(args[0])
    for palabra in contador:
      if contador[palabra] == 1:
        print(f"La palabra '{palabra}' se repite {contador[palabra]} vez")
      else:
        print(f"La palabra '{palabra}' se repite {contador[palabra]} veces")
  
  elif opción == "reemplazar":
    nuevo_texto = reemplazar_palabras(args[0], args[1], args[2])
    print(f"El resultado de sustituir {args[1]} por {args[2]} es:")
    print(f"{nuevo_texto} \n")

  elif opción == "eliminar":
    nuevo_texto = eliminar_palabra(args[0], args[1])
    print(f"El resultado eliminar '{args[1]}' del texto es:")
    print(f"{nuevo_texto} \n")
    
  else:
    print(f"Opción {opción} no válida")
    
  

texto_a_procesar = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."


procesar_texto("contar", texto_a_procesar)

procesar_texto("reemplazar", texto_a_procesar, "texto", "relato")

procesar_texto("eliminar", texto_a_procesar, "ejemplo")

procesar_texto("otra_acción")