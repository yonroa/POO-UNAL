import math

class Calculos:

  @staticmethod
  def calcular_cuadrado(num):
    return (math.pow(num, 2))

  @staticmethod
  def calcular_cubo(num):
    return (math.pow(num, 3))

num = float(input("Ingrese el número:"))

print(f"El cuadrado del número {num} es: {Calculos.calcular_cuadrado(num)}")
print(f"El cubo del número {num} es: {Calculos.calcular_cubo(num)}")
