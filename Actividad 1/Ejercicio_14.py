class Calculos:

  def calcular_cuadrado(num):
    return (num**2)

  def calcular_cubo(num):
    return (num**3)

num = float(input("Ingrese el número:"))

print(f"El cuadrado del número {num} es: {Calculos.calcular_cuadrado(num)}")
print(f"El cubo del número {num} es: {Calculos.calcular_cubo(num)}")
