from enum import Enum

class Automovil:

  class TipoCombustible(Enum):
    GASOLINA = 'GASOLINA'
    BIOETANOL = 'BIOETANOL'
    DIESEL = 'DIESEL'
    BIODISESEL = 'BIODIESEL'
    GAS_NATURAL = 'GAS NATURAL'

  class TipoAutomovil(Enum):
    CIUDAD = 'CIUDAD'
    SUBCOMPACTO = 'SUBCOMPACTO'
    COMPACTO = 'COMPACTO'
    FAMILIAR = 'FAMILIAR'
    EJECUTIVO = 'EJECUTIVO'
    SUV = 'SUV'

  class TipoColor(Enum):
    BLANCO = 'BLANCO'
    NEGRO = 'NEGRO'
    ROJO = 'ROJO'
    NARANJA = 'NARANJA'
    AMARILLO = 'AMARILLO'
    VERDE = 'VERDE'
    AZUL = 'AZUL'
    VIOLETA = 'VIOLETA'

  def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color):
    self.marca = marca
    self.modelo = modelo
    self.motor = motor
    self.tipo_combustible = tipo_combustible
    self.tipo_automovil = tipo_automovil
    self.numero_puertas = numero_puertas
    self.cantidad_asientos = cantidad_asientos
    self.velocidad_maxima = velocidad_maxima
    self.color = color
    self.velocidad_actual = 0

  def get_marca(self):
    return self.marca

  def get_modelo(self):
    return self.modelo

  def get_motor(self):
    return self.motor

  def get_tipo_combustible(self):
    return self.tipo_combustible

  def get_tipo_automovil(self):
    return self.tipo_automovil

  def get_numero_puertas(self):
    return self.numero_puertas

  def get_cantidad_asientos(self):
    return self.cantidad_asientos

  def get_velocidad_maxima(self):
    return self.velocidad_maxima

  def get_color(self):
    return self.color

  def get_velocidad_actual(self):
    return self.velocidad_actual

  def set_marca(self, marca):
    self.marca = marca

  def set_modelo(self, modelo):
    self.modelo = modelo

  def set_motor(self, motor):
    self.motor = motor

  def set_tipo_combustible(self, tipo_combustible):
    self.tipo_combustible = tipo_combustible

  def set_tipo_automovil(self, tipo_automovil):
    self.tipo_automovil = tipo_automovil

  def set_numero_puertas(self, numero_puertas):
    self.numero_puertas = numero_puertas

  def set_cantidad_asientos(self, cantidad_asientos):
    self.cantidad_asientos = cantidad_asientos

  def set_velocidad_maxima(self, velocidad_maxima):
    self.velocidad_maxima = velocidad_maxima

  def set_color(self, color):
    self.color = color

  def set_velocidad_actual(self, velocidad_actual):
    self.velocidad_actual = velocidad_actual


  def acelerar(self, incremento_velocidad):
    if self.velocidad_actual + incremento_velocidad < self.velocidad_maxima:
        self.velocidad_actual += incremento_velocidad
    else:
        print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

  def desacelerar(self, decremento_velocidad):
    if self.velocidad_actual - decremento_velocidad > 0:
        self.velocidad_actual -= decremento_velocidad
    else:
        print("No se puede decrementar a una velocidad negativa.")

  def frenar(self):
    self.velocidad_actual = 0

  def calcular_tiempo_llegada(self, distancia):
    if self.velocidad_actual > 0:
        return (distancia / self.velocidad_actual)

  def imprimir(self):
    print(f"Marca = {self.marca}")
    print(f"Modelo = {self.modelo}")
    print(f"Motor = {self.motor}")
    print(f"Tipo de combustible = {self.tipo_combustible.value}")
    print(f"Tipo de automóvil = {self.tipo_automovil.value}")
    print(f"Número de puertas = {self.numero_puertas}")
    print(f"Cantidad de asientos = {self.cantidad_asientos}")
    print(f"Velocidad máxima = {self.velocidad_maxima}")
    print(f"Color = {self.color.value}")

class EjercicioN23:
  def main():
    auto1 = Automovil("Ford", 2018, 3, Automovil.TipoCombustible.DIESEL,
        Automovil.TipoAutomovil.EJECUTIVO, 5, 6, 250, Automovil.TipoColor.NEGRO)
    auto1.imprimir()

    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.frenar()
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.desacelerar(20)

  if __name__ == "__main__":
    main()
