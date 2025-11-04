import tkinter as tk
from tkinter import messagebox

class EquipoMaratonProgramacion:

    def __init__(self, nombre_equipo, universidad, lenguage_programacion,
                 programadores, tamaño_equipo):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguage_programacion = lenguage_programacion
        self.programadores = programadores
        self.tamaño_equipo = tamaño_equipo


    def equipo_lleno(self):
        return self.tamaño_equipo >= 3
    
    def añadir(self, programador):
        if (self.equipo_lleno()):
            raise Exception("El equipo esta completo. No se puede agregar otro programador.")
        self.programadores.append(programador)
        self.tamaño_equipo += 1

    def validar_label(self, label):
        if len(label) > 20:
            messagebox.showerror("Error Nombre", "El nombre no puede contener mas de 20 caracteres.")
            raise Exception("El nombre no puede contener mas de 20 caracteres.")
        for letra in label:
            if letra.isdigit():
                messagebox.showerror("Error Nombre", "El nombre no puede tener digitos.")
                raise Exception("El nombre no puede tener digitos.")
            
class Programador:

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Equipo Maratón")
        self.geometry("400x450")
        self.resizable(False, False)
        
        self.campos_equipo = {}
        self.campos_programador = {}
        self.equipo = None

        self.btn_nuevo_equipo = None
        
        self.crear_componentes()

    def crear_componentes(self):
        
        frame_equipo = tk.LabelFrame(self, text="Datos del Equipo", padx=10, pady=10)
        frame_equipo.pack(padx=10, pady=10, fill="x")

        datos_equipo = ["Nombre del equipo", "Universidad", "Lenguaje de programación"]
        for i, texto in enumerate(datos_equipo):
            lbl = tk.Label(frame_equipo, text=f"{texto}:")
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            ent = tk.Entry(frame_equipo, width=30)
            ent.grid(row=i, column=1, padx=5, pady=5, sticky="e")
            self.campos_equipo[texto] = ent
        
        self.btn_crear_equipo = tk.Button(frame_equipo, text="Crear Equipo", command=self.crear_equipo)
        self.btn_crear_equipo.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.frame_integrantes = tk.LabelFrame(self, text="Agregar Integrantes (0/3)", padx=10, pady=10)
        self.frame_integrantes.pack(padx=10, pady=10, fill="x")
        
        datos_prog = ["Nombre del integrante", "Apellidos del integrante"]
        for i, texto in enumerate(datos_prog):
            lbl = tk.Label(self.frame_integrantes, text=f"{texto}:")
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            ent = tk.Entry(self.frame_integrantes, width=30, state=tk.DISABLED)
            ent.grid(row=i, column=1, padx=5, pady=5, sticky="e")
            self.campos_programador[texto] = ent
        
        self.btn_añadir = tk.Button(self.frame_integrantes, text="Añadir Programador", command=self.añadir_programador, state=tk.DISABLED)
        self.btn_añadir.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.lbl_resumen = tk.Label(self, text="Equipo NO creado.", fg="red")
        self.lbl_resumen.pack(pady=5)

        self.btn_nuevo_equipo = tk.Button(self, text="Registrar Nuevo Equipo", command=self.reiniciar_registro, state=tk.DISABLED)
        self.btn_nuevo_equipo.pack(pady=10)


    def crear_equipo(self):
        try:
            nombre = self.campos_equipo["Nombre del equipo"].get()
            universidad = self.campos_equipo["Universidad"].get()
            lenguaje = self.campos_equipo["Lenguaje de programación"].get()
            programadores = []
            tamaño_equipo = 0
            
            if not all([nombre, universidad, lenguaje]):
                raise ValueError("Todos los campos del equipo son obligatorios.")

            for campo in [nombre, universidad, lenguaje]:
                EquipoMaratonProgramacion.validar_label(self, campo)

            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje, programadores, tamaño_equipo)
            
            for ent in self.campos_equipo.values():
                ent.config(state=tk.DISABLED)
            self.btn_crear_equipo.config(state=tk.DISABLED)
            
            self.habilitar_integrantes()
            
            messagebox.showinfo("Éxito", f"Equipo '{nombre}' creado. ¡Añada 3 programadores!")
            
        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))

    def habilitar_integrantes(self):
        self.frame_integrantes.config(text="Agregar Integrantes (0/3)")
        for ent in self.campos_programador.values():
            ent.config(state=tk.NORMAL)
        self.btn_añadir.config(state=tk.NORMAL)
        self.lbl_resumen.config(text="Equipo en formación.", fg="blue")

    def añadir_programador(self):
        if not self.equipo:
            return
            
        try:
            nombre_prog = self.campos_programador["Nombre del integrante"].get()
            apellidos_prog = self.campos_programador["Apellidos del integrante"].get()
            
            if not all([nombre_prog, apellidos_prog]):
                raise ValueError("Nombre y apellidos del integrante son obligatorios.")
            
            EquipoMaratonProgramacion.validar_label(self, nombre_prog)
            EquipoMaratonProgramacion.validar_label(self, apellidos_prog)
            
            programador = Programador(nombre_prog, apellidos_prog)
            self.equipo.añadir(programador)
            
            for ent in self.campos_programador.values():
                ent.delete(0, tk.END)
                
            conteo = len(self.equipo.programadores)
            self.frame_integrantes.config(text=f"Agregar Integrantes ({conteo}/3)")
            
            if self.equipo.equipo_lleno():
                self.finalizar_registro()
            
        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))

    def finalizar_registro(self):
        """Bloquea la interfaz al completar el equipo."""
        for ent in self.campos_programador.values():
            ent.config(state=tk.DISABLED)
        self.btn_añadir.config(state=tk.DISABLED)
        self.frame_integrantes.config(text=f"Equipo Completo ({len(self.equipo.programadores)}/3)", fg="green")
        
        nombres = [str(p.nombre) for p in self.equipo.programadores]
        resumen_final = f"Equipo '{self.equipo.nombre_equipo}' registrado.\nIntegrantes: {', '.join(nombres)}"
        self.lbl_resumen.config(text=resumen_final, fg="darkgreen")

        self.btn_nuevo_equipo.config(state=tk.NORMAL)
        messagebox.showinfo("Registro Finalizado", "El equipo ha sido registrado con éxito.")

    def reiniciar_registro(self):
        for ent in self.campos_equipo.values():
            ent.delete(0, tk.END)
        for ent in self.campos_programador.values():
            ent.delete(0, tk.END)
            
        self.equipo = None
        
        for ent in self.campos_equipo.values():
            ent.config(state=tk.NORMAL)
        self.btn_crear_equipo.config(state=tk.NORMAL)
        
        for ent in self.campos_programador.values():
            ent.config(state=tk.DISABLED)
        self.btn_añadir.config(state=tk.DISABLED)
        
        self.frame_integrantes.config(text="Agregar Integrantes (0/3)")
        self.lbl_resumen.config(text="Equipo NO creado.", fg="red")
        self.btn_nuevo_equipo.config(state=tk.DISABLED)
        
        messagebox.showinfo("Nuevo Registro", "Campos limpiados. Listo para registrar un nuevo equipo.")


class Principal:

  def main():
    app = VentanaPrincipal()
    app.mainloop()

  if __name__ == "__main__":
    main()
