"""
Ejercicio 8. Función encontrar_puesto_empleado :
Descripción del ejercicio:
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
Caso de uso:
empleados = [{"nombre": "Juan", "apellido": "García", "puesto": "Secretario"},
{"nombre": "Mabel", "apellido": "García", "puesto": "Product Manager"},
{"nombre": "Isabel", "apellido": "Martín", "puesto": "CEO"}]
"""

def puesto(empleado_a_buscar):
    
    empleados = [{"nombre": "Juan", "apellido": "García", "puesto": "Secretario"},
                {"nombre": "Mabel", "apellido": "García", "puesto": "Product Manager"},
                {"nombre": "Isabel", "apellido": "Martín", "puesto": "CEO"}]
    
    for empleado in empleados:
      if empleado["nombre"]+" "+empleado["apellido"] == empleado_a_buscar:
        print(f"El puesto de {empleado_a_buscar} es {empleado["puesto"]}")
        return
    
    print(f"{empleado_a_buscar} no trabaja aquí")
    
    
  
nombre_completo = "Juan García"
nombre_buscado = puesto(nombre_completo)

nombre_completo = "Ana Lopez"
nombre_buscado = puesto(nombre_completo)
