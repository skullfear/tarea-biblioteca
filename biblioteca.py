from estudiante import *
from docente import *
from administrador import *

class Biblioteca:
    def __init__(self, archivo):
        self.archivo = archivo
        self.libros = []
        self.libros_prestados = []
        self.usuario = None

    def cargar_libros(self):
        try:
            with open(self.archivo, 'r') as archivo_txt:
                for linea in archivo_txt:
                    partes = linea.strip().split(', ')
                    if len(partes) == 3:
                        titulo, autor, ano = partes
                        self.libros.append({'Título': titulo, 'Autor': autor, 'Año de Publicación': ano})
        except FileNotFoundError:
            print(f'El archivo "{self.archivo}" no se encontró.')

    def mostrar_libros(self):
        if self.libros:
            for i, libro in enumerate(self.libros, start=1):
                print(f'Libro {i}:')
                for campo, valor in libro.items():
                    print(f'{campo}: {valor}')
                print('-' * 20)
        else:
            print('No se han cargado libros.')

    def asignar_usuario(self, usuario):
        self.usuario = usuario

    def mostrar_informacion_usuario(self):
        if self.usuario:
            print("\nInformación del usuario:")
            print(self.usuario)
        else:
            print("No se ha asignado ningún usuario.")

    def solicitar_libro(self, numero_libro):
        if 1 <= numero_libro <= len(self.libros):
            libro_solicitado = self.libros[numero_libro - 1]
            if libro_solicitado not in self.libros_prestados:
                self.libros_prestados.append(libro_solicitado)
                print(f'Has solicitado el libro número {numero_libro}:')
                for campo, valor in libro_solicitado.items():
                    print(f'{campo}: {valor}')
            else:
                print('Este libro ya ha sido prestado.')
        else:
            print('Número de libro no válido. Por favor, elige un número de libro válido.')


if __name__ == "__main__":
    while True:
        print("Selecciona tu tipo de usuario:")
        print("1. Estudiante")
        print("2. Docente")
        print("3. Administrador")
        print("4. Salir")
        tipo_usuario = input("Ingresa el número correspondiente: ")

        if tipo_usuario == '4':
            break

        if tipo_usuario == '1':
            usuario = Estudiante()
        elif tipo_usuario == '2':
            usuario = Docente()
        elif tipo_usuario == '3':
            usuario = Administrador()
        else:
            print("Tipo de usuario no válido.")
            continue

        biblioteca = Biblioteca("libros.txt")
        biblioteca.cargar_libros()
        biblioteca.asignar_usuario(usuario)

        while True:
            biblioteca.mostrar_informacion_usuario()
            biblioteca.mostrar_libros()

            try:
                numero_solicitud = int(input('Ingrese el número del libro que desea solicitar, 0 para cambiar de usuario o -1 para salir: '))
                if numero_solicitud == 0:
                    break
                elif numero_solicitud == -1:
                    exit()
                biblioteca.solicitar_libro(numero_solicitud)
            except ValueError:
                print('Entrada no válida. Debes ingresar un número válido.')
