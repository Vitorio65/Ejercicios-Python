'''
Ejercicio 15. Clase UsuarioBanco :
Explicación del ejercicio:
Descripción:
Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones
como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Alicia".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
'''
class UsuarioBanco:
  def __init__(self,nombre_usuario, saldo_usuario, cuenta_corriente):
    self.nombre_usuario = nombre_usuario
    self.saldo_usuario = saldo_usuario
    self.cuenta_corriente = cuenta_corriente
  
     
  def retirar_dinero(self, importe):
    try:
     if self.saldo_usuario < importe:
       print("Saldo insuficiente")
     elif not self.cuenta_corriente:
       print ("No tiene cuenta corriente")
     else:
       self.saldo_usuario -= importe
       print(f"{self.nombre_usuario}: Cantidad {importe} retirada correctamtente")
       print(f"Su nuevo saldo en cc {self.saldo_usuario}\n")
    
    except Exception as e:
      print(f"No se puede realizar esta operación: {e}\n")       
  
  def transferir_dinero(self,usuario_destino, importe):
    try:
      if self.saldo_usuario < importe:
        print("Saldo insuficiente")
      elif not self.cuenta_corriente:
         print ("No tiene cuenta corriente")
      else:
        usuario_destino.agregar_dinero(importe)
        self.saldo_usuario -= importe
        print(f"Se ha transferido {importe} de {self.nombre_usuario} a {usuario_destino.nombre_usuario}")
      
    except Exception as e:
      print(f"No se puede realizar esta operación: {e}\n")   
  
  def agregar_dinero(self, importe):
     try:
       self.saldo_usuario += importe
       print(f"{self.nombre_usuario}: se han agredado a su cc {importe}")
       print(f"Su nuevo saldo es {self.saldo_usuario} \n")
     except Exception as e:
       print(f"No se ha podido agregar la cantidad {e}")
       

  
  def mostrar_saldo (self):
    print(f"Nombre del usuario: {self.nombre_usuario}")
    print(f"Saldo del usuario: {self.saldo_usuario}")
    print(f"Cuenta corriente: {self.cuenta_corriente}\n")

# --------------------------------------------------------

usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)
  
  
usuario1.mostrar_saldo()
usuario2.mostrar_saldo()

usuario1.agregar_dinero(20)

usuario2.transferir_dinero(usuario1, 50)

usuario1.retirar_dinero(50)

usuario1.mostrar_saldo()
usuario2.mostrar_saldo()

  
  