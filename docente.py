class Docente:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del docente: ")
        self.titulo = input("Ingrese el título del docente: ")

    def __str__(self):
        return f"Nombre del docente: {self.nombre}\nTítulo del docente: {self.titulo}"