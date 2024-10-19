'''
Ejercicio 12. Función numeros_suma usando lambdas y
map :
Descripción del ejercicio:

Crea una función lambda que sume 3 a cada número de una lista dada.
Caso de uso: lista_numeros = [24, 56, 2.3, 19, -1, 0]
'''
lista_numeros = [24, 56, 2.3, 19, -1, 0]

sumar_3 = list(map(lambda x: x + 3, lista_numeros))

print(lista_numeros)
print(sumar_3)