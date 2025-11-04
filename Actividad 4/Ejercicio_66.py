import math
import tkinter as tk
from tkinter import messagebox

class ArithmeticException(Exception):
    """Excepción personalizada para errores aritméticos."""
    pass

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo(valor: float) -> float:
        """Calcula el logaritmo natural del valor si es positivo."""
        if valor <= 0:
            raise ArithmeticException("El valor debe ser un número positivo para calcular el logaritmo")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> float:
        """Calcula la raíz cuadrada del valor si es positivo."""
        if valor < 0:
            raise ArithmeticException("El valor debe ser un número positivo para calcular la raíz cuadrada")
        return math.sqrt(valor)

# --- Función que se ejecuta al presionar el botón ---
def calcular():
    resultado_text.delete(1.0, tk.END)
    try:
        valor_texto = entry_valor.get().strip()
        if not valor_texto:
            messagebox.showwarning("Advertencia", "Debe ingresar un número.")
            return

        valor = float(valor_texto)
        resultado_text.insert(tk.END, f"Valor numérico = {valor}\n")

        try:
            log = CalculosNumericos.calcular_logaritmo(valor)
            resultado_text.insert(tk.END, f"Logaritmo neperiano: {log}\n")
        except ArithmeticException as e:
            resultado_text.insert(tk.END, f"{e}\n")

        try:
            raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)
            resultado_text.insert(tk.END, f"Raíz cuadrada: {raiz}\n")
        except ArithmeticException as e:
            resultado_text.insert(tk.END, f"{e}\n")

    except ValueError:
        messagebox.showerror("Error", "Debe ingresar un número válido.")

# --- Interfaz gráfica principal ---
ventana = tk.Tk()
ventana.title("Cálculos Numéricos")
ventana.geometry("400x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Ingrese un número:", font=("Arial", 11, "bold")).pack(pady=(20, 5))
entry_valor = tk.Entry(ventana, width=20, font=("Arial", 11))
entry_valor.pack(pady=5)

tk.Button(
    ventana,
    text="Calcular",
    command=calcular,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15
).pack(pady=10)

resultado_text = tk.Text(ventana, width=50, height=10, wrap=tk.WORD)
resultado_text.pack(pady=10)

ventana.mainloop()
