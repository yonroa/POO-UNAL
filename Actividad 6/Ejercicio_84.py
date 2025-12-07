from enum import Enum
import tkinter as tk
from tkinter import filedialog, Menu, messagebox, ttk
import os

class TipoCargo(Enum):
    DIRECTIVO = "DIRECTIVO"
    ESTRATEGICO = "ESTRATEGICO"
    OPERATIVO = "OPERATIVO"

class TipoGenero(Enum):
    MASCULINO = "MASCULINO"
    FEMENINO = "FEMENINO"
    OTRO = "OTRO"

class Empleado:
    def __init__(self, nombre: str, apellidos: str, cargo: TipoCargo, genero: TipoGenero, salarioDia: float, 
                 diasTrabajados: int, otrosIngresos: float, pagoSalud: float, aportePensiones: float):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salarioDia = salarioDia
        self.diasTrabajados = diasTrabajados
        self.otrosIngresos = otrosIngresos
        self.pagoSalud = pagoSalud
        self.aportePensiones = aportePensiones

    def getNombre(self) -> str:
        return self.nombre
    
    def getApellidos(self) -> str:
        return self.apellidos
    
    def getCargo(self) -> TipoCargo:
        return self.cargo
    
    def getGenero(self) -> TipoGenero:
        return self.genero
    
    def getSalarioDia(self) -> float:
        return self.salarioDia
    
    def getDiasTrabajados(self) -> int:
        return self.diasTrabajados
    
    def getOtrosIngresos(self) -> float:
        return self.otrosIngresos
    
    def getPagoSalud(self) -> float:
        return self.pagoSalud
    
    def getAportePensiones(self) -> float:
        return self.aportePensiones

    def calcularNomina(self) -> float:
        return ((self.salarioDia * self.diasTrabajados) + (self.otrosIngresos - self.pagoSalud - self.aportePensiones))

class ListaEmpleados:
    def __init__(self):
        self.empleados = []
        self.totalNomina = 0

    def agregarEmpleado(self, empleado: Empleado):
        self.empleados.append(empleado)

    def calcularTotalNomina(self) -> float:
        total_nomina = 0
        for empleado in self.empleados:
            total_nomina += empleado.calcularNomina()
        return total_nomina
    
    def obtenerMatriz(self):
        datos = []
        total_nomina_calculada = 0
        
        for empleado in self.empleados:
            nomina_empleado = empleado.calcularNomina()
            sueldo_formateado = f"{nomina_empleado:,.2f}"
            
            datos.append([
                empleado.getNombre(),
                empleado.getApellidos(),
                sueldo_formateado
            ])
            
            total_nomina_calculada += nomina_empleado

        self.totalNomina = total_nomina_calculada 
        return datos

    def convertirTexto(self) -> str:
        texto = ""
        for empleado in self.empleados:
            texto += (f"Nombre: {empleado.getNombre()},\n Apellidos: {empleado.getApellidos()},\n "
                      f"Cargo: {empleado.getCargo().value},\n Genero: {empleado.getGenero().value},\n "
                      f"Salario: ${empleado.getSalarioDia()},\n Dias Trabajados: {empleado.getDiasTrabajados()},\n "
                      f"Otros Ingresos: ${empleado.getOtrosIngresos()},\n Pagos Salud: ${empleado.getPagoSalud()},\n "
                      f"Aporte Pensiones: ${empleado.getAportePensiones()}\n"
                      f"-------------------------------\n")
        texto += f"Total Nomina: ${self.calcularTotalNomina()}\n"
        return texto
    
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.empleados = ListaEmpleados() 
        self.inicio()
        self.title("Nomina")
        self.geometry("280x380")
        self.resizable(False, False)

    def inicio(self):
        barraMenu = Menu(self)
        self.config(menu=barraMenu)

        menuOpciones = Menu(barraMenu, tearoff=0)

        menuOpciones.add_command(
            label="Agregar empleado", 
            command=self.gestionar_agregar_empleado
        )
        
        menuOpciones.add_command(
            label="Calcular nómina", 
            command=self.gestionar_calcular_nomina
        )
        
        menuOpciones.add_separator() 
        
        menuOpciones.add_command(
            label="Guardar archivo", 
            command=self.gestionar_guardar_archivo
        )
        
        barraMenu.add_cascade(label="Menú", menu=menuOpciones)

    def gestionar_agregar_empleado(self):
        ventana_agregar = VentanaAgregarEmpleado(self.empleados)

    def gestionar_calcular_nomina(self):
        ventana_nomina = VentanaNomina(self.empleados)
        
    def gestionar_guardar_archivo(self):
        directorio_elegido = filedialog.askdirectory(
            title="Seleccionar Directorio para Guardar"
        )

        if directorio_elegido:
            try:
                contenido = self.empleados.convertirTexto()

                nombre_archivo = "Nomina.txt"
                ruta_completa = os.path.join(directorio_elegido, nombre_archivo)
                
                with open(ruta_completa, 'w') as f:
                    f.write(contenido) 

                texto = f"El archivo de la nómina {nombre_archivo} se ha creado en {directorio_elegido}"
                messagebox.showinfo(
                    title="Mensaje", 
                    message=texto
                )
                
            except Exception as e:
                messagebox.showerror(
                    title="Error de Archivo", 
                    message=f"Ocurrió un error al guardar el archivo: {e}"
                )

class VentanaAgregarEmpleado(tk.Toplevel):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        self.inicio()
        
        self.title("Agregar Empleado")
        self.geometry("300x400")
        self.resizable(False, False)
        
        self.transient(self.master)
        self.grab_set()
        self.focus_set()

    def inicio(self):
        self.nombre = tk.Label(self, text="Nombre:")
        self.nombre.place(x=20, y=20, width=135, height=23)
        self.campoNombre = tk.Entry(self)
        self.campoNombre.place(x=160, y=20, width=100, height=23)
        
        self.apellidos = tk.Label(self, text="Apellidos:")
        self.apellidos.place(x=20, y=50, width=135, height=23)
        self.campoApellidos = tk.Entry(self)
        self.campoApellidos.place(x=160, y=50, width=100, height=23)
        
        self.cargo = tk.Label(self, text="Cargo:")
        self.cargo.place(x=20, y=80, width=135, height=23)
        
        cargos = ["Directivo", "Estratégico", "Operativo"]
        self.campoCargo = ttk.Combobox(self, values=cargos, state="readonly")
        self.campoCargo.current(0)
        self.campoCargo.place(x=160, y=80, width=100, height=23)

        self.genero = tk.Label(self, text="Genero:")
        self.genero.place(x=20, y=110, width=100, height=30)
        
        self.tipo_genero_var = tk.StringVar(value="Masculino")
        
        self.masculino = tk.Radiobutton(self, text="Masculino", 
                                        variable=self.tipo_genero_var, value="Masculino")
        self.masculino.place(x=160, y=110, width=100, height=30)
        
        self.femenino = tk.Radiobutton(self, text="Femenino", 
                                       variable=self.tipo_genero_var, value="Femenino")
        self.femenino.place(x=160, y=140, width=100, height=30)

        self.salarioDia = tk.Label(self, text="Salario por dia:")
        self.salarioDia.place(x=20, y=170, width=135, height=23)
        self.campoSalarioDia = tk.Entry(self)
        self.campoSalarioDia.place(x=160, y=170, width=100, height=23)
        
        self.númeroDias = tk.Label(self, text="Dias trabajados al mes:")
        self.númeroDias.place(x=20, y=200, width=135, height=23)
        
        self.campoNúmeroDias = tk.Spinbox(self, from_=1, to=31, 
                                          increment=1, wrap=False, width=3)
        self.campoNúmeroDias.delete(0, "end")
        self.campoNúmeroDias.insert(0, 30)
        self.campoNúmeroDias.place(x=160, y=200, width=40, height=23)
        
        self.otrosIngresos = tk.Label(self, text="Otros ingresos:")
        self.otrosIngresos.place(x=20, y=230, width=135, height=23)
        self.campoOtrosIngresos = tk.Entry(self)
        self.campoOtrosIngresos.place(x=160, y=230, width=100, height=23)
        
        self.aportesSalud = tk.Label(self, text="Pagos por salud:")
        self.aportesSalud.place(x=20, y=260, width=135, height=23)
        self.campoAportesSalud = tk.Entry(self)
        self.campoAportesSalud.place(x=160, y=260, width=100, height=23)
        
        self.pensiones = tk.Label(self, text="Aportes pensiones:")
        self.pensiones.place(x=20, y=290, width=135, height=23)
        self.campoPensiones = tk.Entry(self)
        self.campoPensiones.place(x=160, y=290, width=100, height=23)
        
        self.agregar = tk.Button(self, text="Agregar", command=self.añadirEmpleado)
        self.agregar.place(x=20, y=320, width=100, height=23)
        
        self.limpiar = tk.Button(self, text="Borrar", command=self.limpiarCampos)
        self.limpiar.place(x=160, y=320, width=80, height=23)

    def limpiarCampos(self):
        self.campoNombre.delete(0, tk.END)
        self.campoApellidos.delete(0, tk.END)
        self.campoSalarioDia.delete(0, tk.END)
        
        self.campoNúmeroDias.delete(0, tk.END)
        self.campoNúmeroDias.insert(0, 0)
        
        self.campoOtrosIngresos.delete(0, tk.END)
        self.campoAportesSalud.delete(0, tk.END)
        self.campoPensiones.delete(0, tk.END)

    def añadirEmpleado(self):
        try:
            item_seleccionado = self.campoCargo.get()
            
            if item_seleccionado == "Directivo":
                tipoC = TipoCargo.DIRECTIVO
            elif item_seleccionado == "Estratégico":
                tipoC = TipoCargo.ESTRATEGICO
            else:
                tipoC = TipoCargo.OPERATIVO
                
            genero_seleccionado = self.tipo_genero_var.get()
            
            if genero_seleccionado == "Masculino":
                tipoG = TipoGenero.MASCULINO
            else:
                tipoG = TipoGenero.FEMENINO
                
            nombre = self.campoNombre.get()
            apellidos = self.campoApellidos.get()
            
            salarioDia = float(self.campoSalarioDia.get())
            
            numeroDias = int(self.campoNúmeroDias.get())
            
            otrosIngresos = float(self.campoOtrosIngresos.get())
            aporteSalud = float(self.campoAportesSalud.get())
            pensiones = float(self.campoPensiones.get())
            
            e = Empleado(nombre, apellidos, tipoC, tipoG, salarioDia, numeroDias, otrosIngresos, aporteSalud, pensiones)
            self.lista.agregarEmpleado(e)
            
            messagebox.showinfo(
                title="Mensaje", 
                message="El empleado ha sido agregado"
            )
            
            self.limpiarCampos()
            
        except ValueError:
            messagebox.showerror(
                title="Error", 
                message="Campo nulo o error en formato de número (verifique que los campos numéricos contengan solo números)."
            )
        except Exception as e:
            messagebox.showerror(
                title="Error", 
                message=f"Ocurrió un error inesperado: {e}"
            )

class VentanaNomina(tk.Toplevel):
    def __init__(self, lista):
        super().__init__()
        
        self.lista = lista
        
        self.inicio()
        
        self.title("Nomina de Empleados")
        self.geometry("350x250")
        self.resizable(False, False)
        
        self.transient(self.master)
        self.grab_set()
        self.focus_set()

    def inicio(self):
        self.empleados = tk.Label(self, text="Lista de empleados:")
        self.empleados.place(x=20, y=10, width=135, height=23)
        
        datos = self.lista.obtenerMatriz() 
        
        titulos = ["NOMBRE", "APELLIDOS", "SUELDO"]
        
        self.tabla = ttk.Treeview(self, columns=titulos, show='headings', height=5)

        for col in titulos:
            self.tabla.heading(col, text=col)
            if col == "SUELDO":
                self.tabla.column(col, anchor='e', width=100)
            else:
                self.tabla.column(col, anchor='w', width=90)
        
        for fila in datos:
            self.tabla.insert('', tk.END, values=fila)
        
        self.tabla.place(x=20, y=50, width=310, height=100) 

        self.nómina = tk.Label(self, anchor='w')
        
        total_nomina = self.lista.totalNomina
        
        texto_nomina = f"Total nómina mensual = $ {total_nomina:,.2f}"
        
        self.nómina.config(text=texto_nomina)
        
        self.nómina.place(x=20, y=160, width=250, height=23)


class Principal:

  def main():
    app = VentanaPrincipal()
    app.mainloop()

  if __name__ == "__main__":
    main()
