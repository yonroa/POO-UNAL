import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:
  def __init__(self):
    self.volumen = 0.0
    self.superficie = 0.0

  def set_volumen(self, volumen):
    self.volumen = float(volumen)

  def set_superficie(self, superficie):
    self.superficie = float(superficie)

  def get_volumen(self):
    return self.volumen

  def get_superficie(self):
    return self.superficie


class Cilindro(FiguraGeometrica):
  def __init__(self, radio, altura):
    super().__init__()
    self.radio = float(radio)
    self.altura = float(altura)
    self.set_volumen(self.calcular_volumen())
    self.set_superficie(self.calcular_superficie())

  def calcular_volumen(self):
    return math.pi * (math.pow(self.radio, 2)) * self.altura

  def calcular_superficie(self):
    area_lateral = 2.0 * math.pi * self.radio * self.altura
    area_bases = 2.0 * math.pi * (math.pow(self.radio, 2))
    return area_lateral + area_bases


class Esfera(FiguraGeometrica):
  def __init__(self, radio):
    super().__init__()
    self.radio = float(radio)
    self.set_volumen(self.calcular_volumen())
    self.set_superficie(self.calcular_superficie())

  def calcular_volumen(self):
    return (4.0 / 3.0) * math.pi * (math.pow(self.radio, 3))

  def calcular_superficie(self):
    return 4.0 * math.pi * (math.pow(self.radio, 2))


class Piramide(FiguraGeometrica):
  def __init__(self, base, altura, apotema):
    super().__init__()
    self.base = float(base)
    self.altura = float(altura)
    self.apotema = float(apotema)
    self.set_volumen(self.calcular_volumen())
    self.set_superficie(self.calcular_superficie())

  def calcular_volumen(self):
    return (math.pow(self.base, 2)) * self.altura / 3.0

  def calcular_superficie(self):
    area_base = math.pow(self.base, 2)
    area_lados = 2.0 * self.base * self.apotema
    return area_base + area_lados


class VentanaCilindro(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.title("Cilindro")
    self.geometry("300x190")
    self.resizable(False, False)

    tk.Label(self, text="Radio (cm):").grid(row=0, column=0, padx=10, pady=8, sticky="w")
    self.campo_radio = tk.Entry(self, width=12, justify="right")
    self.campo_radio.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(self, text="Altura (cm):").grid(row=1, column=0, padx=10, pady=8, sticky="w")
    self.campo_altura = tk.Entry(self, width=12, justify="right")
    self.campo_altura.grid(row=1, column=1, padx=10, pady=8)

    self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
    self.btn_calcular.grid(row=2, column=0, columnspan=2, pady=8)

    self.lbl_volumen = tk.Label(self, text="Volumen (cm³): ")
    self.lbl_volumen.grid(row=3, column=0, columnspan=2, padx=10, sticky="w")

    self.lbl_superficie = tk.Label(self, text="Superficie (cm²): ")
    self.lbl_superficie.grid(row=4, column=0, columnspan=2, padx=10, sticky="w")

  def calcular(self):
    try:
      r = float(self.campo_radio.get().strip().replace(",", "."))
      h = float(self.campo_altura.get().strip().replace(",", "."))
      cilindro = Cilindro(r, h)
      self.lbl_volumen.config(text=f"Volumen (cm³): {cilindro.calcular_volumen():.2f}")
      self.lbl_superficie.config(text=f"Superficie (cm²): {cilindro.calcular_superficie():.2f}")
    except Exception:
      messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaEsfera(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.title("Esfera")
    self.geometry("300x170")
    self.resizable(False, False)

    tk.Label(self, text="Radio (cm):").grid(row=0, column=0, padx=10, pady=8, sticky="w")
    self.campo_radio = tk.Entry(self, width=12, justify="right")
    self.campo_radio.grid(row=0, column=1, padx=10, pady=8)

    self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
    self.btn_calcular.grid(row=1, column=0, columnspan=2, pady=8)

    self.lbl_volumen = tk.Label(self, text="Volumen (cm³): ")
    self.lbl_volumen.grid(row=2, column=0, columnspan=2, padx=10, sticky="w")

    self.lbl_superficie = tk.Label(self, text="Superficie (cm²): ")
    self.lbl_superficie.grid(row=3, column=0, columnspan=2, padx=10, sticky="w")

  def calcular(self):
    try:
      r = float(self.campo_radio.get().strip().replace(",", "."))
      esfera = Esfera(r)
      self.lbl_volumen.config(text=f"Volumen (cm³): {esfera.calcular_volumen():.2f}")
      self.lbl_superficie.config(text=f"Superficie (cm²): {esfera.calcular_superficie():.2f}")
    except Exception:
      messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPiramide(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.title("Pirámide")
    self.geometry("320x220")
    self.resizable(False, False)

    tk.Label(self, text="Base (cm):").grid(row=0, column=0, padx=10, pady=6, sticky="w")
    self.campo_base = tk.Entry(self, width=12, justify="right")
    self.campo_base.grid(row=0, column=1, padx=10, pady=6)

    tk.Label(self, text="Altura (cm):").grid(row=1, column=0, padx=10, pady=6, sticky="w")
    self.campo_altura = tk.Entry(self, width=12, justify="right")
    self.campo_altura.grid(row=1, column=1, padx=10, pady=6)

    tk.Label(self, text="Apotema (cm):").grid(row=2, column=0, padx=10, pady=6, sticky="w")
    self.campo_apotema = tk.Entry(self, width=12, justify="right")
    self.campo_apotema.grid(row=2, column=1, padx=10, pady=6)

    self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
    self.btn_calcular.grid(row=3, column=0, columnspan=2, pady=8)

    self.lbl_volumen = tk.Label(self, text="Volumen (cm³): ")
    self.lbl_volumen.grid(row=4, column=0, columnspan=2, padx=10, sticky="w")

    self.lbl_superficie = tk.Label(self, text="Superficie (cm²): ")
    self.lbl_superficie.grid(row=5, column=0, columnspan=2, padx=10, sticky="w")

  def calcular(self):
    try:
      b = float(self.campo_base.get().strip().replace(",", "."))
      h = float(self.campo_altura.get().strip().replace(",", "."))
      a = float(self.campo_apotema.get().strip().replace(",", "."))
      piramide = Piramide(b, h, a)
      self.lbl_volumen.config(text=f"Volumen (cm³): {piramide.calcular_volumen():.2f}")
      self.lbl_superficie.config(text=f"Superficie (cm²): {piramide.calcular_superficie():.2f}")
    except Exception:
      messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPrincipal(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Figuras")
    self.geometry("360x140")
    self.resizable(False, False)

    cont = tk.Frame(self)
    cont.pack(expand=True, fill="both", padx=10, pady=10)

    btn_cil = tk.Button(cont, text="Cilindro", width=12, command=self.abrir_cilindro)
    btn_cil.grid(row=0, column=0, padx=8, pady=10)

    btn_esf = tk.Button(cont, text="Esfera", width=12, command=self.abrir_esfera)
    btn_esf.grid(row=0, column=1, padx=8, pady=10)

    btn_pir = tk.Button(cont, text="Pirámide", width=12, command=self.abrir_piramide)
    btn_pir.grid(row=0, column=2, padx=8, pady=10)

  def abrir_cilindro(self):
    VentanaCilindro(self)

  def abrir_esfera(self):
    VentanaEsfera(self)

  def abrir_piramide(self):
    VentanaPiramide(self)


class Principal:

  def main():
    app = VentanaPrincipal()
    app.mainloop()

  if __name__ == "__main__":
    main()
