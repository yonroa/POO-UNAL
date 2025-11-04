class PruebaExcepciones:

    @staticmethod
    def main():
        try:
            print("Ingresando al primer try")
            cociente = 10000 / 0 
            print("Después de la division")
        except ZeroDivisionError:
            print("Division por cero")
        finally:
            print("Ingresando al primer finally")

        try:
            print("Ingresando al segundo try")
            objeto = None
            objeto.toString()
            print("Imprimiendo objeto")
        except ZeroDivisionError:
            print("División por cero")
        except Exception:
            print("Ocurrio una excepcion")
        finally:
            print("Ingresando al segundo finally")

if __name__ == "__main__":
    PruebaExcepciones.main()
