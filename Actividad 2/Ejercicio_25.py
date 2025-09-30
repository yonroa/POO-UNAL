from enum import Enum

class CuentaBancaria:

  class tipoCuenta(Enum):
    AHORROS = 'AHORROS'
    CORRIENTE = 'CORRIENTE'

  def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
      self.nombres = nombres
      self.apellidos = apellidos
      self.numero_cuenta = numero_cuenta
      self.tipo_cuenta = tipo_cuenta
      self.saldo = 0.0

  def imprimir_informacion(self):
      print("----- Información de la Cuenta -----")
      print(f"Titular: {self.nombres} {self.apellidos}")
      print(f"Número de cuenta: {self.numero_cuenta}")
      print(f"Tipo de cuenta: {self.tipo_cuenta.value}")
      print(f"Saldo actual: ${self.saldo:.2f}")

  def consultar_saldo(self):
      print(f"Saldo actual: ${self.saldo:.2f}")
      return self.saldo

  def consignar(self, valor):
      if valor > 0:
          self.saldo += valor
          print(f"Se consignaron ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
      else:
          print("El valor a consignar debe ser positivo.")

  def retirar(self, valor):
      if valor <= 0:
          print("El valor a retirar debe ser positivo.")
      elif valor > self.saldo:
          print("Fondos insuficientes. No se puede realizar el retiro.")
      else:
          self.saldo -= valor
          print(f"Se retiraron ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")

class EjercicioN25:
  
  def main():
    cuenta = CuentaBancaria("Juan", "Pérez", 123456789, CuentaBancaria.tipoCuenta.AHORROS)

    cuenta.imprimir_informacion()
    cuenta.consignar(500)
    cuenta.retirar(200)
    cuenta.consultar_saldo()
    cuenta.retirar(400)
  
  if __name__ == "__main__":
    main()
