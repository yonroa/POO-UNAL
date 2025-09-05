import math

class Calculos:

  @staticmethod
  def calcular_suma(suma, x):
    return (suma + x)

  @staticmethod
  def calcular_x(x, y):
    return (x + (math.pow(y, 2)))

  @staticmethod
  def calcular_suma_final(suma, x, y):
    return (suma + (x / y))

x = float(input('Escriba el valor de x: '))
suma = float(input('Escriba el valor de SUMA: '))
y = float(input('Escriba el valor de Y: '))

suma = Calculos.calcular_suma(suma, x)
x = Calculos.calcular_x(x, y)
suma = Calculos.calcular_suma_final(suma, x, y)

print("EL VALOR DE LA SUMA ES: ", suma)
