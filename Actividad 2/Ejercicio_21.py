class Persona:

  def __init__(self, nombre, apellidos, numeroDocumentoIdentidad, añoNacimiento):
    self.nombre = nombre
    self.apellidos = apellidos
    self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
    self.añoNacimiento = añoNacimiento

  def imprimir(self):
    print(f"Nombre = {self.nombre}")
    print(f"Apellidos = {self.apellidos}")
    print(f"Numero de documento de identidad = {self.numeroDocumentoIdentidad}")
    print(f"Año de nacimiento = {self.añoNacimiento}")
    print()

class EjercicioN21:
  def main():
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)
    p1.imprimir()
    p2.imprimir()

  if __name__ == "__main__":
    main()
