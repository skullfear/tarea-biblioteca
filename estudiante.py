class Estudiante:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.codigo_identificacion = input("Ingrese un código de identificación de 11 números: ")
        while not self.validar_codigo_identificacion(self.codigo_identificacion):
            print("El código de identificación debe contener 11 números.")
            self.codigo_identificacion = input("Ingrese un código de identificación de 11 números: ")

    def validar_codigo_identificacion(self, codigo):
        return codigo.isdigit() and len(codigo) == 11

    def __str__(self):
        return f"Nombre del estudiante: {self.nombre}\nCódigo de identificación: {self.codigo_identificacion}"