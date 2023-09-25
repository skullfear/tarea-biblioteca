class Administrador:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del administrador: ")
        self.nivel_acceso = input("Ingrese el nivel de acceso del administrador (1, 2 o 3): ")
        while not self.validar_nivel_acceso(self.nivel_acceso):
            print("El nivel de acceso debe ser 1, 2 o 3.")
            self.nivel_acceso = input("Ingrese el nivel de acceso del administrador (1, 2 o 3): ")
            
    def validar_nivel_acceso(self, nivel):
        return nivel.isdigit() and nivel in ['1', '2', '3']

    def __str__(self):
        return f"Nombre del administrador: {self.nombre}\nNivel de acceso: {self.nivel_acceso}"