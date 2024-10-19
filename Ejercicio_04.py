'''
Ejercicio 4. Función enmascarado_datos :
Descripción del ejercicio:
Crea una función que convierta una variable en una cadena de texto y
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
'''

def enmascarar_valor(variable):
  texto = str(variable)
  enmascarado =""
  posicion = 0
  while posicion < len(texto):
    if  posicion < len(texto) -4:
      enmascarado += texto[posicion]
    else:
      enmascarado += "#"
    posicion += 1
  return (enmascarado)

variable = str(input("Introduce una variable: "))

valor_enmascarado = enmascarar_valor (variable)

print (f"La cadena enmascararada es {valor_enmascarado}")
