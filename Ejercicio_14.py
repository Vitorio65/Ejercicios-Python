'''
Ejercicio 14. No te vayas por las ramas :
Explicación del ejercicio:
Descripción:
Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
'''

class arbol:
  def __init__(self):
    self.tronco = 1
    self.ramas = list()
    
  def crecer_tronco(self):
    # 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    self.tronco += 1
    
  def nueva_rama(self):
    #3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    self.ramas.append(1)
  
  def crecer_ramas(self):
    #4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    self.ramas = [x + 1 for x in self.ramas]
    
  def quitar_rama(self, rama):
    #5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    if 0 <= rama < len(self.ramas):
        self.ramas.pop(rama)
    else:
        print("Índice fuera de rango")
    
  
  def info_arbol(self):
    #6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
    info = f"Longitud del tronco: {self.tronco}\n"
    info += f"Número de ramas: {len(self.ramas)}\n"
    info += f"Longitudes de las ramas: {self.ramas}"
    print(info)
    return info
    
mi_arbol = arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.crecer_ramas()
mi_arbol.crecer_ramas()
mi_arbol.crecer_ramas()
mi_arbol.info_arbol()
mi_arbol.quitar_rama(0)
mi_arbol.info_arbol()    