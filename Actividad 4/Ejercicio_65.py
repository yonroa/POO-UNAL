import tkinter as tk
from tkinter import messagebox

class IllegalArgumentException(Exception):
    pass

class Vendedor:
    def __init__(self, nombre: str, apellidos: str, edad: int):
        self.verificar_edad(edad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def imprimir(self):
        return (f"Datos del vendedor:\n"
                f"Nombre: {self.nombre}\n"
                f"Apellidos: {self.apellidos}\n"
                f"Edad: {self.edad}")

    def verificar_edad(self, edad: int):
        if edad < 0 or edad > 120:
            raise IllegalArgumentException("La edad no puede ser negativa ni mayor a 120")
        if edad < 18:
            raise IllegalArgumentException("El vendedor debe ser mayor de 18 años")

def crear_vendedor():
    try:
        nombre = entry_nombre.get().strip()
        apellidos = entry_apellidos.get().strip()
        edad_texto = entry_edad.get().strip()

        if not nombre or not apellidos or not edad_texto:
            messagebox.showwarning("Advertencia", "Debe llenar todos los campos.")
            return

        edad = int(edad_texto)
        vendedor = Vendedor(nombre, apellidos, edad)

        messagebox.showinfo("Éxito", "Vendedor creado exitosamente.")
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, vendedor.imprimir())

    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero válido.")
    except IllegalArgumentException as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("400x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Nombre:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Apellidos:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
entry_apellidos = tk.Entry(ventana, width=40)
entry_apellidos.pack(pady=5)

tk.Label(ventana, text="Edad:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
entry_edad = tk.Entry(ventana, width=10)
entry_edad.pack(pady=5)

tk.Button(ventana, text="Crear Vendedor", command=crear_vendedor, bg="#4CAF50", fg="white",
          font=("Arial", 10, "bold")).pack(pady=15)

resultado_text = tk.Text(ventana, width=45, height=8, wrap=tk.WORD)
resultado_text.pack(pady=10)

ventana.mainloop()
