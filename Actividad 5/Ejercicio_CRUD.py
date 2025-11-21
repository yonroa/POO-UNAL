import tkinter as tk
from tkinter import messagebox

class Amigo:

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.validar_nombre()
        self.validar_telefono()

    def validar_nombre(self):
        if len(self.nombre) > 30:
            messagebox.showerror("Error Nombre", "El nombre no puede tener más de 30 caracteres.")
            raise ValueError("El nombre no puede tener más de 30 caracteres.")
        if any(char.isdigit() for char in self.nombre):
            messagebox.showerror("Error Nombre", "El nombre no puede contener dígitos.")
            raise ValueError("El nombre no puede contener dígitos.")
        
    def validar_telefono(self):
        if not self.telefono.isdigit():
            messagebox.showerror("Error Teléfono", "El teléfono debe contener solo dígitos.")
            raise ValueError("El teléfono debe contener solo dígitos.")
    
    def __str__(self):
        return f"{self.nombre}:{self.telefono}"

class CrearAmigo:

    def __init__(self, amigo):
        self.amigo = amigo

    def guardar(self, ruta="amigos.txt"):
        nombre_nuevo = self.amigo.nombre.strip().lower()
        telefono_nuevo = self.amigo.telefono.strip()
        try:
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        if ":" in line:
                            nombre_existente, telefono_existente = line.split(":", 1)
                            if nombre_existente.strip().lower() == nombre_nuevo:
                                return (False, f"Ya existe un amigo con el nombre '{self.amigo.nombre}'.")
                            if telefono_existente.strip() == telefono_nuevo:
                                return (False, f"Ya existe un amigo con el teléfono '{self.amigo.telefono}'.")
            except FileNotFoundError:
                pass

            with open(ruta, "a", encoding="utf-8") as f:
                f.write(str(self.amigo) + "\n")
            return (True, None)
        except Exception as e:
            return (False, f"Error al guardar: {e}")
        
class BuscarAmigo:

    def __init__(self, query):
        self.nombre = query[0]
        self.telefono = query[1]

    def buscar(self, ruta="amigos.txt"):
        resultados = []
        nombre_buscar = self.nombre.strip().lower()
        telefono_buscar = self.telefono.strip()
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or ":" not in line:
                        continue
                    nombre, telefono = line.split(":", 1)
                    if nombre_buscar and nombre.lower() == nombre_buscar:
                        resultados.append((nombre, telefono))
                        continue
                    if telefono_buscar and telefono.strip() == telefono_buscar:
                        resultados.append((nombre, telefono))
            return resultados
        except FileNotFoundError:
            return []


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Amigos")
        self.geometry("520x280")
        self.resizable(False, False)
        self.crear_componentes()

    def crear_componentes(self):
        self.columnconfigure(0, weight=1)

        lbl_nombre = tk.Label(self, text="Nombre", anchor="center")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.cmp_nombre = tk.Entry(self, width=20, justify="center")
        self.cmp_nombre.grid(row=1, column=0, padx=5, pady=5)

        lbl_numero = tk.Label(self, text="Telefono", anchor="center")
        lbl_numero.grid(row=2, column=0, padx=5, pady=5)
        self.cmp_numero = tk.Entry(self, width=20, justify="center")
        self.cmp_numero.grid(row=3, column=0, padx=5, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.grid(row=4, column=0, pady=15)

        btn_crear = tk.Button(btn_frame, text="Crear amigo", width=14, command=self.crear_amigo)
        btn_crear.pack(side="left", padx=3)

        btn_buscar = tk.Button(btn_frame, text="Buscar amigo", width=14, command=self.buscar_amigo)
        btn_buscar.pack(side="left", padx=3)

        btn_actualizar = tk.Button(btn_frame, text="Actualizar amigo", width=14, command=self.actualizar_amigo)
        btn_actualizar.pack(side="left", padx=3)

        btn_borrar = tk.Button(btn_frame, text="Borrar amigo", width=14, command=self.borrar_amigo)
        btn_borrar.pack(side="left", padx=3)

    def crear_amigo(self):
        nombre = self.cmp_nombre.get().strip()
        telefono = self.cmp_numero.get().strip()
        if not nombre or not telefono:
            messagebox.showwarning("Crear amigo", "Ingrese nombre y teléfono para crear un amigo.")
            return

        amigo = Amigo(nombre, telefono)
        creador = CrearAmigo(amigo)
        ok, msg = creador.guardar()
        if ok:
            messagebox.showinfo("Crear amigo", f"Amigo creado: {nombre} - {telefono}")
            self.cmp_nombre.delete(0, tk.END)
            self.cmp_numero.delete(0, tk.END)
        else:
            if msg:
                messagebox.showerror("Crear amigo", msg)
            else:
                messagebox.showerror("Crear amigo", "Error al guardar el amigo en el archivo.")

    def buscar_amigo(self):
        nombre = self.cmp_nombre.get().strip()
        numero = self.cmp_numero.get().strip()
        query = [nombre, numero]
        if query == ['', '']:
            messagebox.showwarning("Buscar amigo", "Ingrese el nombre o teléfono a buscar.")
            return

        buscador = BuscarAmigo(query)
        resultados = buscador.buscar()

        if not resultados:
            messagebox.showinfo("Buscar amigo", "No se encontraron coincidencias.")
            return

        texto = "\n".join([f"Nombre: {n} - Telefono: {t}" for n, t in resultados])
        messagebox.showinfo("Buscar amigo - Coincidencias", texto)

    def actualizar_amigo(self):
        nombre = self.cmp_nombre.get().strip()
        telefono = self.cmp_numero.get().strip()
        if not nombre:
            messagebox.showwarning("Actualizar amigo", "Ingrese el nombre del amigo a actualizar.")
            return
        messagebox.showinfo("Actualizar amigo", f"Actualizar: {nombre} - {telefono}")

    def borrar_amigo(self):
        nombre = self.cmp_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Borrar amigo", "Ingrese el nombre del amigo a borrar.")
            return
        # confirmación simple
        if messagebox.askyesno("Borrar amigo", f"¿Eliminar a {nombre}?"):
            messagebox.showinfo("Borrar amigo", f"{nombre} eliminado.")

class Principal:

    def main():
        app = VentanaPrincipal()
        app.mainloop()

    if __name__ == "__main__":
        main()
