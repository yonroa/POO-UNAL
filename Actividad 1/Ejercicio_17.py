import math

class Calculos:

  @staticmethod
  def calcular_area(radio):
    return (math.pi * (math.pow(radio, 2)))

  @staticmethod
  def calcular_longitud(radio):
    return (2 * math.pi * radio)

radio = float(input("Ingrese el radio: "))

print("El radio del circulo es: ", radio)
print("El area del circulo es: ", Calculos.calcular_area(radio))
print("La longitud del circulo es: ", Calculos.calcular_longitud(radio))
