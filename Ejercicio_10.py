'''
Ejercicio 10. Función resto_division usando lambdas:
Descripción del ejercicio:
Crea una función lambda que calcule el resto de la división entre dos números dados.
'''
resto_división = lambda x, y: x % y

núm1 = int(input ("Introduce dividendo: "))
núm2 = int(input ("Introduce divisor: "))

cociente = resto_división (núm1, núm2)
print(f"El resto de la división {núm1} entre {núm2} es {cociente}")