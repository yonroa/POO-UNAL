import tkinter as tk
from tkinter import filedialog, messagebox

class LectorArchivo:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_contenido(self):
        if not self.ruta_archivo:
            return []
            
        contenido = []
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    contenido.append(linea) 
            return contenido
                
        except FileNotFoundError:
            raise FileNotFoundError("El archivo no se encontró en la ruta especificada.")
        except Exception as e:
            raise Exception(f"Error al leer el archivo: {e}")

class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lector de Archivos")
        self.geometry("600x400")
        
        self.lector = LectorArchivo("")
        
        self.crear_componentes()

    def crear_componentes(self):
        
        self.lbl_ruta = tk.Label(self, text="Archivo seleccionado: Ninguno", anchor="w", wraplength=580)
        self.lbl_ruta.pack(padx=10, pady=(10, 5), fill="x")

        self.btn_seleccionar = tk.Button(self, text="Seleccionar Archivo", command=self.seleccionar_archivo)
        self.btn_seleccionar.pack(pady=5)
        
        self.txt_contenido = tk.Text(self, wrap="word", state=tk.DISABLED)
        self.txt_contenido.pack(padx=10, pady=10, fill="both", expand=True)
        
    def seleccionar_archivo(self):

        ruta = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt")]
        )
        
        if ruta:
            self.lector.ruta_archivo = ruta
            self.lbl_ruta.config(text=f"Archivo seleccionado: {ruta}")
            
            self.mostrar_contenido()
        else:
            messagebox.showinfo("Información", "Selección de archivo cancelada.")

    def mostrar_contenido(self):
        self.txt_contenido.config(state=tk.NORMAL)
        self.txt_contenido.delete("1.0", tk.END)
        
        try:
            lineas = self.lector.leer_contenido()
            
            contenido_completo = "".join(lineas)
            self.txt_contenido.insert(tk.END, contenido_completo)
            
        except FileNotFoundError as e:
            messagebox.showerror("Error de Archivo", str(e))
        except Exception as e:
            messagebox.showerror("Error de Lectura", str(e))

        self.txt_contenido.config(state=tk.DISABLED)
    
        
class Principal:

    def main():
        app = VentanaPrincipal()
        app.mainloop()

    if __name__ == "__main__":
        main()
