class Calculos:

  @staticmethod
  def calcular_edad_alberto(edad_juan):
    return ((2 * edad_juan) / 3)

  @staticmethod
  def calcular_edad_ana(edad_juan):
    return ((4 * edad_juan) / 3)

  @staticmethod
  def calcular_edad_mama(edad_juan, edad_alberto, edad_ana):
    return (edad_juan + edad_alberto + edad_ana)

edad_juan = int(input("La edad de Juan es: "))

edad_alberto = Calculos.calcular_edad_alberto(edad_juan)
edad_ana = Calculos.calcular_edad_ana(edad_juan)
edad_mama = Calculos.calcular_edad_mama(edad_juan, edad_alberto, edad_ana)

print("La edad de Alberto es:", int(edad_alberto))
print("La edad de Ana es:", int(edad_ana))
print("La edad de la mama es:", int(edad_mama))
