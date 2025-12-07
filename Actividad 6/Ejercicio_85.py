import tkinter as tk
from tkinter import Menu, messagebox, simpledialog
from datetime import datetime


class Huesped:

    def __init__(self, nombres: str, apellidos: str, documentoIdentidad: int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documentoIdentidad = documentoIdentidad

    def setFechaSalida(self, fechaSalida: datetime.date) -> None:
        self.fechaSalida = fechaSalida
    
    def setFechaIngreso(self, fechaIngreso: datetime.date) -> None:
        self.fechaIngreso = fechaIngreso
    
    def getFechaIngreso(self) -> datetime.date:
        return self.fechaIngreso
    
    def obtenerDiasAlojamiento(self) -> int:
        return (self.fechaSalida - self.fechaIngreso).days


class Habitacion:

    def __init__(self, numeroHabitacion: int, disponible: bool, precioDia: float):
        self.numeroHabitacion = numeroHabitacion
        self.disponible = disponible
        self.precioDia = precioDia

    def getNumeroHabitacion(self) -> int:
        return self.numeroHabitacion
    
    def getDisponible(self) -> bool:
        return self.disponible
    
    def getPrecioDia(self) -> float:
        return self.precioDia
    
    def getHuesped(self) -> Huesped:
        return self.huesped
    
    def setHuesped(self, huesped: Huesped):
        self.huesped = huesped

    def setDisponible(self, disponible: bool):
        self.disponible = disponible


class Hotel:

    def __init__(self):
        self.listaHabitaciones = []
        for i in range(1, 6):
            habitacion = Habitacion(i, True, 120000)
            self.listaHabitaciones.append(habitacion)
        for i in range(6, 11):
            habitacion = Habitacion(i, True, 160000)
            self.listaHabitaciones.append(habitacion)

    def buscarFechaIngresoHabitacion(self, numero: int) -> str:
        for habitacion in self.listaHabitaciones:
            if habitacion.getNumeroHabitacion() == numero:
                fecha = habitacion.getHuesped().getFechaIngreso()
                return fecha.strftime("%d/%m/%Y")
        return ""
        
    def buscarHabitacionOcupada(self, numero: int) -> bool:
        for habitacion in self.listaHabitaciones:
            if (habitacion.getNumeroHabitacion() == numero and not habitacion.getDisponible()):
                return True
        return False


class VentanaSalida(tk.Toplevel):

    def __init__(self, hotel, numero):
        super().__init__()
        self.hotel = hotel
        self.numeroHabitacion = numero
        self.posicionHabitacion = -1
        self.habitacionOcupada = None
        self.dias_alojamiento = 0
        self.valor_total = 0.0
        self.inicio()
        self.title("Salida Huespedes")
        self.geometry("260x260")
        self.resizable(False, False)  

    def inicio(self):
        habitacion = tk.Label(self, text=f"Habitacion: {self.numeroHabitacion}", anchor='w')
        habitacion.grid(row=0, column=0, sticky='ew', padx=3, pady=3)

        fecha_ingreso_str = self.hotel.buscarFechaIngresoHabitacion(self.numeroHabitacion)

        self.fechaIngreso = tk.Label(self, text=f"Fecha de ingreso: {fecha_ingreso_str}", anchor='w')
        self.fechaIngreso.grid(row=1, column=0, sticky='ew', padx=3, pady=3)

        fechaSalida_label = tk.Label(self, text="Fecha de salida (aaaa-mm-dd):", anchor='w')
        fechaSalida_label.grid(row=2, column=0, sticky='ew', padx=3, pady=3)

        self.campoFechaSalida = tk.Entry(self)
        self.campoFechaSalida.grid(row=3, column=0, sticky='ew', padx=3, pady=3)

        self.calcular = tk.Button(self, text="Calcular", command=self.gestionar_calcular)
        self.calcular.grid(row=4, column=0, sticky='ew', padx=3, pady=5)

        self.cantidadDias = tk.Label(self, text="Cantidad de dias: 0", anchor='w')
        self.cantidadDias.grid(row=5, column=0, sticky='ew', padx=3, pady=3)

        self.totalPago = tk.Label(self, text="Total: $0.00", anchor='w', font=('Arial', 10, 'bold'))
        self.totalPago.grid(row=6, column=0, sticky='ew', padx=3, pady=3)

        self.registrarSalida = tk.Button(self, text="Registrar Salida", command=self.gestionar_registrar_salida)
        self.registrarSalida.grid(row=7, column=0, sticky='ew', padx=3, pady=5)

        self.registrarSalida.config(state=tk.DISABLED)

        self.grid_columnconfigure(0, weight=1)

    def buscar_habitacion_ocupada(self):
        for i, habitacion_obj in enumerate(self.hotel.listaHabitaciones):
            if habitacion_obj.getNumeroHabitacion() == self.numeroHabitacion:
                self.posicionHabitacion = i
                self.habitacionOcupada = habitacion_obj
                return True
        return False

    def gestionar_calcular(self):
        fechaS_str = self.campoFechaSalida.get()
        if self.posicionHabitacion == -1 and not self.buscar_habitacion_ocupada():
            messagebox.showerror("Error", "No se pudo encontrar la habitacion ocupada.")
            return

        try:
            fecha_salida_dt = datetime.strptime(fechaS_str, "%Y-%m-%d").date()
            huesped_obj = self.habitacionOcupada.getHuesped()
            if huesped_obj is None:
                 raise Exception("Huesped no encontrado en la habitacion.")
                 
            fecha_ingreso_dt = huesped_obj.getFechaIngreso()
            
            if fecha_ingreso_dt < fecha_salida_dt:
                
                huesped_obj.setFechaSalida(fecha_salida_dt)
                
                self.dias_alojamiento = huesped_obj.obtenerDiasAlojamiento()
                
                self.cantidadDias.config(text=f"Cantidad de dias: {self.dias_alojamiento}")
                
                precio_dia = self.habitacionOcupada.getPrecioDia()
                self.valor_total = self.dias_alojamiento * precio_dia
                
                self.totalPago.config(text=f"Total: ${self.valor_total:,.2f}")
                
                self.registrarSalida.config(state=tk.NORMAL)
                
            else:
                messagebox.showerror(
                    "Mensaje", 
                    "La fecha de salida es menor o igual que la de ingreso"
                )
                self.registrarSalida.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror(
                "Mensaje", 
                "La fecha no está en el formato solicitado (debe ser aaaa-mm-dd)."
            )
            self.registrarSalida.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
            self.registrarSalida.config(state=tk.DISABLED)

    def gestionar_registrar_salida(self):
        if self.habitacionOcupada is None or self.posicionHabitacion == -1:
            messagebox.showerror("Error", "Error interno: Habitacion no identificada.")
            return
            
        self.habitacionOcupada.setHuesped(None) 
        self.habitacionOcupada.setDisponible(True) 
        self.hotel.listaHabitaciones[self.posicionHabitacion] = self.habitacionOcupada
        
        messagebox.showinfo("Mensaje", "Se ha registrado la salida del huesped")
        self.destroy()


class VentanaIngreso(tk.Toplevel):

    def __init__(self, hotel, numeroHabitacionReservada):
        super().__init__()
        self.hotel = hotel
        self.numeroHabitacionReservada = numeroHabitacionReservada
        self.habitacionReservada = None
        self.inicio()
        self.title("Ingreso")
        self.geometry("290x250") 
        self.resizable(False, False)

        # Configuracion para hacer la ventana modal
        self.transient(self.master)
        self.grab_set()
        self.focus_set()

    def inicio(self):
        habitacion = tk.Label(self, 
                              text=f"Habitacion: {self.numeroHabitacionReservada}", 
                              anchor='w')
        habitacion.grid(row=0, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

        fechaIngreso = tk.Label(self, text="Fecha (aaaa-mm-dd):", anchor='w')
        fechaIngreso.grid(row=1, column=0, sticky='w', padx=5, pady=3)
        
        self.campoFechaIngreso = tk.Entry(self)
        self.campoFechaIngreso.grid(row=1, column=1, sticky='ew', padx=5, pady=3)
        
        huesped_label = tk.Label(self, text="Huesped", anchor='w', font=('Arial', 10, 'bold'))
        huesped_label.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=(10, 3))
        
        nombre = tk.Label(self, text="Nombre:", anchor='w')
        nombre.grid(row=3, column=0, sticky='w', padx=5, pady=3)
        
        self.campoNombre = tk.Entry(self)
        self.campoNombre.grid(row=3, column=1, sticky='ew', padx=5, pady=3)
        
        apellidos = tk.Label(self, text="Apellidos:", anchor='w')
        apellidos.grid(row=4, column=0, sticky='w', padx=5, pady=3)

        self.campoApellidos = tk.Entry(self)
        self.campoApellidos.grid(row=4, column=1, sticky='ew', padx=5, pady=3)
        
        documentoIdentidad = tk.Label(self, text="Doc. Identidad:", anchor='w')
        documentoIdentidad.grid(row=5, column=0, sticky='w', padx=5, pady=3)
        
        self.campoDocumentoIdentidad = tk.Entry(self)
        self.campoDocumentoIdentidad.grid(row=5, column=1, sticky='ew', padx=5, pady=3)
        
        self.aceptar = tk.Button(self, text="Aceptar", command=self.gestionar_aceptar)
        self.aceptar.grid(row=6, column=0, sticky='ew', padx=5, pady=10)
        
        self.cancelar = tk.Button(self, text="Cancelar", command=self.gestionar_cancelar)
        self.cancelar.grid(row=6, column=1, sticky='ew', padx=5, pady=10)
        
        self.grid_columnconfigure(1, weight=1)

    def gestionar_aceptar(self):
        fechaIngresada_str = self.campoFechaIngreso.get()
        nombre_str = self.campoNombre.get().strip()
        apellidos_str = self.campoApellidos.get().strip()
        documento_str = self.campoDocumentoIdentidad.get().strip()
        
        try:
            if not all([fechaIngresada_str, nombre_str, apellidos_str, documento_str]):
                 raise ValueError("Campo nulo o vacío.")
            documento_int = int(documento_str)
            
            fecha = datetime.strptime(fechaIngresada_str, "%Y-%m-%d").date()
            
        except ValueError as e: 
            messagebox.showerror(
                "Error", 
                "Campo nulo o error en formato de numero (Doc. Identidad y formato de fecha)."
            )
            return
        except TypeError: 
            messagebox.showerror(
                "Mensaje", 
                "La fecha no está en el formato solicitado (debe ser aaaa-mm-dd)."
            )
            return

        posicion = -1
        habitacion_encontrada = None
        
        for i, habitacion_obj in enumerate(self.hotel.listaHabitaciones):
            if habitacion_obj.getNumeroHabitacion() == self.numeroHabitacionReservada:
                posicion = i
                habitacion_encontrada = habitacion_obj
                
        if habitacion_encontrada:
            try:
                huesped_obj = Huesped(nombre_str, apellidos_str, documento_int)
                huesped_obj.setFechaIngreso(fecha) 
                habitacion_encontrada.setHuesped(huesped_obj)
                habitacion_encontrada.setDisponible(False) 
                self.hotel.listaHabitaciones[posicion] = habitacion_encontrada

                messagebox.showinfo("Mensaje", "El huesped ha sido registrado")
                
                self.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar: {e}")
        else:
             messagebox.showerror("Error", "No se encontró la habitacion en la lista.")


    def gestionar_cancelar(self):
        self.destroy()


class VentanaHabitaciones(tk.Toplevel):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.etiquetas_disponibles = {}
        self.inicio()
        self.title("Habitaciones")
        self.geometry("760x260")
        self.resizable(False, False)

        self.transient(self.master)
        self.grab_set()
        self.focus_set()

    def inicio(self):
        for i in range(1, 11):
            habitacion_obj = self.hotel.listaHabitaciones[i - 1]
            if i <= 5:
                x_pos = 20 + (i - 1) * 140
                y_base = 30
            else:
                x_pos = 20 + (i - 6) * 140 
                y_base = 120
            estado = "Disponible" if habitacion_obj.getDisponible() else "No disponible"

            tk.Label(self, text=f"Habitacion {i}").place(x=x_pos, y=y_base, width=130, height=23)

            disponible_label = tk.Label(self, text=estado)
            disponible_label.place(x=x_pos, y=y_base + 20, width=100, height=23)

            self.etiquetas_disponibles[i] = disponible_label 

        self.habitacionSeleccionada = tk.Label(self, text="Habitacion a reservar:")
        self.habitacionSeleccionada.place(x=250, y=180, width=135, height=23)

        self.campoHabitacionSeleccionada = tk.Spinbox(
            self, 
            from_=1, 
            to=10, 
            increment=1, 
            wrap=False,
            width=3
        )
        self.campoHabitacionSeleccionada.delete(0, tk.END)
        self.campoHabitacionSeleccionada.insert(0, 1)
        self.campoHabitacionSeleccionada.place(x=380, y=180, width=40, height=23)
        
        self.botonAceptar = tk.Button(self, text="Aceptar", command=self.gestionar_aceptar)
        self.botonAceptar.place(x=500, y=180, width=100, height=23)

    def gestionar_aceptar(self):
        try:
            habitacion_str = self.campoHabitacionSeleccionada.get()
            habitacion_num = int(habitacion_str)

            if not (1 <= habitacion_num <= 10):
                messagebox.showerror("Error", "Numero de habitacion inválido.")
                return

            if not self.hotel.buscarHabitacionOcupada(habitacion_num):
                ventanaIngreso = VentanaIngreso(self.hotel, habitacion_num)
                self.destroy()
            else:
                messagebox.showinfo(
                    "Mensaje", 
                    "La habitacion está ocupada"
                )
        except ValueError:
            messagebox.showerror("Error", "Ingrese un numero de habitacion válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


class VentanaPrincipal(tk.Tk):

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.inicio()
        self.title("Hotel")
        self.geometry("280x380")
        self.resizable(False, False)

    def inicio(self):
        barraMenu = Menu(self)
        self.config(menu=barraMenu)

        menuOpciones = Menu(barraMenu, tearoff=0)

        self.itemMenu1 = "Consultar habitaciones"
        menuOpciones.add_command(
            label=self.itemMenu1, 
            command=self.gestionar_consultar_habitaciones
        )

        self.itemMenu2 = "Salida de huespedes"
        menuOpciones.add_command(
            label=self.itemMenu2, 
            command=self.gestionar_salida_huespedes
        )

        barraMenu.add_cascade(label="Menu", menu=menuOpciones)

    def gestionar_consultar_habitaciones(self):
        ventanaHabitaciones = VentanaHabitaciones(self.hotel)
        
    def gestionar_salida_huespedes(self):
        try:
            numeroHabitacion_str = simpledialog.askstring(
                "Salida de huespedes", 
                "Ingrese numero de habitacion",
                parent=self
            )

            if numeroHabitacion_str is None or numeroHabitacion_str.strip() == "":
                return

            numero = int(numeroHabitacion_str)

            if not (1 <= numero <= 10):
                messagebox.showinfo(
                    "Mensaje", 
                    "El numero de habitacion debe estar entre 1 y 10"
                )
            elif self.hotel.buscarHabitacionOcupada(numero):
                ventanaSalida = VentanaSalida(self.hotel, numero)
                
            else: 
                messagebox.showinfo(
                    "Mensaje", 
                    "La habitacion ingresada no ha sido ocupada"
                )
                
        except ValueError: 
            messagebox.showerror(
                "Error", 
                "Campo nulo o error en formato de numero (debe ingresar un numero entero)."
            )
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")


class Principal:

  def main():
    hotel = Hotel()
    app = VentanaPrincipal(hotel)
    app.mainloop()

  if __name__ == "__main__":
    main()
