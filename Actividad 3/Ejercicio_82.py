import math
import tkinter as tk
from tkinter import messagebox


class Notas:
  def __init__(self):
    self.lista_notas = [0.0] * 5

  def calcular_promedio(self):
    return sum(self.lista_notas) / len(self.lista_notas)

  def calcular_desviacion(self):
    promedio = self.calcular_promedio()
    suma = sum(math.pow((x - promedio), 2) for x in self.lista_notas)
    return math.sqrt(suma / len(self.lista_notas))

  def calcular_menor(self):
    return min(self.lista_notas)

  def calcular_mayor(self):
    return max(self.lista_notas)


class VentanaPrincipal(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Notas")
    self.geometry("280x380")
    self.resizable(False, False)
    self.crear_componentes()

  def crear_componentes(self):
    nota1 = tk.Label(self, text=f"Nota 1:")
    nota1.grid(row=0, column=0, padx=12, pady=8, sticky="w")

    nota2 = tk.Label(self, text=f"Nota 2:")
    nota2.grid(row=1, column=0, padx=12, pady=8, sticky="w")

    nota3 = tk.Label(self, text=f"Nota 3:")
    nota3.grid(row=2, column=0, padx=12, pady=8, sticky="w")

    nota4 = tk.Label(self, text=f"Nota 4:")
    nota4.grid(row=3, column=0, padx=12, pady=8, sticky="w")

    nota5 = tk.Label(self, text=f"Nota 5:")
    nota5.grid(row=4, column=0, padx=12, pady=8, sticky="w")

    campo_nota1 = tk.Entry(self, width=15, justify="right")
    campo_nota1.grid(row=0, column=1, padx=12, pady=8)

    campo_nota2 = tk.Entry(self, width=15, justify="right")
    campo_nota2.grid(row=1, column=1, padx=12, pady=8)

    campo_nota3 = tk.Entry(self, width=15, justify="right")
    campo_nota3.grid(row=2, column=1, padx=12, pady=8)

    campo_nota4 = tk.Entry(self, width=15, justify="right")
    campo_nota4.grid(row=3, column=1, padx=12, pady=8)

    campo_nota5 = tk.Entry(self, width=15, justify="right")
    campo_nota5.grid(row=4, column=1, padx=12, pady=8)

    self.campos = [campo_nota1, campo_nota2, campo_nota3, campo_nota4, campo_nota5]

    self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
    self.btn_calcular.grid(row=5, column=0, padx=12, pady=10, sticky="w")

    self.btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
    self.btn_limpiar.grid(row=5, column=1, padx=12, pady=10, sticky="e")

    self.lbl_promedio = tk.Label(self, text="Promedio = ")
    self.lbl_promedio.grid(row=6, column=0, columnspan=2, padx=12, pady=8, sticky="w")

    self.lbl_desv = tk.Label(self, text="Desviación estándar = ")
    self.lbl_desv.grid(row=7, column=0, columnspan=2, padx=12, pady=8, sticky="w")

    self.lbl_mayor = tk.Label(self, text="Valor mayor = ")
    self.lbl_mayor.grid(row=8, column=0, columnspan=2, padx=12, pady=8, sticky="w")

    self.lbl_menor = tk.Label(self, text="Valor menor = ")
    self.lbl_menor.grid(row=9, column=0, columnspan=2, padx=12, pady=8, sticky="w")

  def leer_notas(self):
    notas = []
    for idx, ent in enumerate(self.campos, start=1):
      texto = ent.get().strip().replace(",", ".")
      if texto == "":
        raise ValueError(f"Falta la Nota {idx}.")
      try:
        notas.append(float(texto))
      except ValueError:
        raise ValueError(f"La Nota {idx} no es un número válido.")
    return notas

  def calcular(self):
    try:
      notas = self.leer_notas()
      modelo = Notas()
      modelo.lista_notas = notas

      prom = modelo.calcular_promedio()
      desv = modelo.calcular_desviacion()
      may = modelo.calcular_mayor()
      men = modelo.calcular_menor()

      self.lbl_promedio.config(text=f"Promedio = {prom:.2f}")
      self.lbl_desv.config(text=f"Desviación estándar = {desv:.2f}")
      self.lbl_mayor.config(text=f"Valor mayor = {may:.2f}")
      self.lbl_menor.config(text=f"Valor menor = {men:.2f}")

    except ValueError as e:
      messagebox.showerror("Entrada inválida", str(e))

  def limpiar(self):
    for ent in self.campos:
      ent.delete(0, tk.END)
    self.lbl_promedio.config(text="Promedio = ")
    self.lbl_desv.config(text="Desviación estándar = ")
    self.lbl_mayor.config(text="Valor mayor = ")
    self.lbl_menor.config(text="Valor menor = ")


class Principal:

  def main():
    app = VentanaPrincipal()
    app.mainloop()

  if __name__ == "__main__":
    main()
