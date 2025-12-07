import tkinter as tk
from tkinter import Menu, messagebox
from tkcalendar import DateEntry
from datetime import datetime


class Contacto:

    def __init__(self, nombres: str, apellidos: str, fechaNacimiento: datetime, direccion: str, telefono: str, correo: str):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo


class ListaContactos:

    def __init__(self):
        self.contactos = []

    def agregarContacto(self, contacto: Contacto) -> None:
        self.contactos.append(contacto)


class VentanaContacto(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Detalles del contacto")
        self.start()

    def start(self):
        grid = self
        grid.columnconfigure(1, weight=1)
        grid.rowconfigure(7, weight=1)
        grid.config(padx=10, pady=10)

        nombres_label = tk.Label(grid, text="Nombres:")
        apellidos_label = tk.Label(grid, text="Apellidos:")
        fechaNacimiento_label = tk.Label(grid, text="Fecha nacimiento:")
        dirección_label = tk.Label(grid, text="Dirección:")
        teléfono_label = tk.Label(grid, text="Teléfono:")
        correo_label = tk.Label(grid, text="Correo:")

        self.campoNombres = tk.Entry(grid)
        self.campoApellidos = tk.Entry(grid)
        self.campoDirección = tk.Entry(grid)
        self.campoTeléfono = tk.Entry(grid)
        self.campoCorreo = tk.Entry(grid)

        self.campoFechaNacimiento = DateEntry(grid, 
                                               selectmode='day', 
                                               date_pattern='yyyy-mm-dd',
                                               width=15, 
                                               background='darkblue', 
                                               foreground='white', 
                                               borderwidth=2)

        self.lista = tk.Listbox(grid, height=10)

        padx_val = 5
        pady_val = 5

        nombres_label.grid(row=0, column=0, sticky='w', padx=padx_val, pady=pady_val)
        apellidos_label.grid(row=1, column=0, sticky='w', padx=padx_val, pady=pady_val)
        fechaNacimiento_label.grid(row=2, column=0, sticky='w', padx=padx_val, pady=pady_val)
        dirección_label.grid(row=3, column=0, sticky='w', padx=padx_val, pady=pady_val)
        teléfono_label.grid(row=4, column=0, sticky='w', padx=padx_val, pady=pady_val)
        correo_label.grid(row=5, column=0, sticky='w', padx=padx_val, pady=pady_val)

        self.campoNombres.grid(row=0, column=1, sticky='ew', padx=padx_val, pady=pady_val)
        self.campoApellidos.grid(row=1, column=1, sticky='ew', padx=padx_val, pady=pady_val)
        self.campoFechaNacimiento.grid(row=2, column=1, sticky='w', padx=padx_val, pady=pady_val)
        self.campoDirección.grid(row=3, column=1, sticky='ew', padx=padx_val, pady=pady_val)
        self.campoTeléfono.grid(row=4, column=1, sticky='ew', padx=padx_val, pady=pady_val)
        self.campoCorreo.grid(row=5, column=1, sticky='ew', padx=padx_val, pady=pady_val)

        self.lista.grid(row=0, column=2, rowspan=7, sticky='nsew', padx=padx_val, pady=pady_val)

        self.agregar = tk.Button(grid, text="Agregar", command=self.mostrarDatos)
        self.agregar.grid(row=6, column=0, columnspan=2, sticky='ew', padx=padx_val, pady=pady_val)
        
    def mostrarDatos(self):
        a = self.campoNombres.get().strip()
        b = self.campoApellidos.get().strip()
        c_date = self.campoFechaNacimiento.get_date()
        d = self.campoDirección.get().strip()
        e = self.campoTeléfono.get().strip()
        f = self.campoCorreo.get().strip()
        if not all([a, b, d, e, f]):
            messagebox.showerror(
                "Error en ingreso de datos", 
                "No se permiten campos vacíos"
            )
        else:
            try:
                contacto = Contacto(a, b, c_date, d, e, f)

                listaContactos = ListaContactos() 
                listaContactos.agregarContacto(contacto)

                data = f"{a} - {b} - {c_date} - {d} - {e} - {f}"
                self.lista.insert(tk.END, data)

                self.campoNombres.delete(0, tk.END)
                self.campoApellidos.delete(0, tk.END)
                self.campoDirección.delete(0, tk.END)
                self.campoTeléfono.delete(0, tk.END)
                self.campoCorreo.delete(0, tk.END)
                
            except Exception as ex:
                messagebox.showerror("Error", f"Error al procesar los datos: {ex}")


class Principal:

  def main():
    app = VentanaContacto()
    app.mainloop()

  if __name__ == "__main__":
    main()
