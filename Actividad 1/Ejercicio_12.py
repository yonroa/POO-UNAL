class Calculos:

  @staticmethod
  def calcular_salario_bruto(horas_labor, valor_hora):
    return (horas_labor * valor_hora)

  @staticmethod
  def calcular_valor_retencion_fuente(porcentaje_retencion, salario_bruto):
    return ((salario_bruto * porcentaje_retencion) / 100)

  @staticmethod
  def calcular_salario_neto(salario_bruto, valor_retencion_fuente):
    return (salario_bruto - valor_retencion_fuente)

horas_labor = float(input('Horas de trabajo a la semana: '))
valor_hora = float(input('Valor de una hora de trabajo: '))
porcentaje_retencion = float(input('Porcentaje de retención en la fuente: '))

salario_bruto = Calculos.calcular_salario_bruto(horas_labor, valor_hora)
valor_retencion_fuente = Calculos.calcular_valor_retencion_fuente(porcentaje_retencion, salario_bruto)
salario_neto = Calculos.calcular_salario_neto(salario_bruto, valor_retencion_fuente)

print(f"El salario bruto es de : {salario_bruto}")
print(f"El valor de la retencion de la fuente es: {valor_retencion_fuente}")
print(f"El salario neto es: {salario_neto}")
