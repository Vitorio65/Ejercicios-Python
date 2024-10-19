'''
Ejercicio 9. Función cubo_numero usando lambdas:
Descripción del ejercicio:
Crea una función que calcule el cubo de un número dado mediante una función lambda
'''

calcular_cubo = lambda x: x ** 3
  
  
  
núm = int(input ("Introduce un número para calcular su cubo: "))
núm_al_cubo = calcular_cubo(núm)
print(f"El valor al cubo de {núm} es {núm_al_cubo}")