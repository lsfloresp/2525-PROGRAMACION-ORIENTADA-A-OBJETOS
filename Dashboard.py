import os
import subprocess

# Dashboard.py - Versión personalizada
# Estudiante: Santiago Flores
# Asignatura: Programación Orientada a Objetos
# Universidad Estatal Amazónica
# Objetivo: Gestionar tareas y proyectos de POO de manera personalizada
# Cambios realizados:
# - Añadido menú de tareas personales usando POO
# - Mejoras de estilo y comentarios en funciones
# - Integración con menú principal


# FUNCIONES ORIGINALES DEL DASHBOARD

def mostrar_codigo(ruta_script):
    """
    Lee y muestra el contenido de un script Python.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en un nuevo terminal.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


#
# SECCIÓN AÑADIDA POR SANTIAGO FLORES
# Menú interactivo para gestionar tareas personales usando POO

class Tarea:
    """
    Representa una tarea personal.
    Atributos:
        nombre: nombre de la tarea
        descripcion: descripción de la tarea
        estado: "Pendiente" o "Completada"
    Métodos:
        marcar_completada(): marca la tarea como completada
    """

    def __init__(self, nombre, descripcion, estado="Pendiente"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def marcar_completada(self):
        self.estado = "Completada"

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} [{self.estado}]"


tareas = []


def menu_tareas():
    """
    Menú interactivo para gestionar tareas personales.
    Opciones:
    1 - Agregar tarea
    2 - Ver tareas
    3 - Marcar tarea como completada
    0 - Regresar al menú principal
    """
    while True:
        print("\n--- Gestión de mis tareas ---")
        print("1 - Agregar tarea")
        print("2 - Ver tareas")
        print("3 - Marcar tarea como completada")
        print("0 - Regresar al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción: ")
            tareas.append(Tarea(nombre, descripcion))
            print(f"Tarea '{nombre}' agregada.")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas registradas.")
            else:
                print("\n--- Tareas registradas ---")
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")

        elif opcion == "3":
            if not tareas:
                print("No hay tareas para completar.")
            else:
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")
                try:
                    idx = int(input("Número de la tarea a completar: ")) - 1
                    if 0 <= idx < len(tareas):
                        tareas[idx].marcar_completada()
                        print(f"Tarea '{tareas[idx].nombre}' completada.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Debes ingresar un número válido.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")



# MENÚ ORIGINAL MEJORADO

def mostrar_menu():
    """
    Menú principal que combina las unidades originales y la sección de tareas.
    """
    ruta_base = os.path.dirname(__file__)
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\n=== Menu Principal - Dashboard ===")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("9 - Gestionar mis tareas")  # nueva opción de tareas
        print("0 - Salir")

        eleccion = input("Elige una unidad, '9' para tareas o '0' para salir: ")

        if eleccion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif eleccion == '9':
            menu_tareas()
        elif eleccion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra subcarpetas dentro de una unidad.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n--- Submenú: Selecciona una subcarpeta ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts .py dentro de una subcarpeta y permite ejecutarlos.
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n--- Scripts: Selecciona un script para ver y ejecutar ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # regresa al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")



# EJECUCIÓN DEL DASHBOARD

if __name__ == "__main__":
    print("Bienvenido al Dashboard de POO - Versión personalizada de Santiago Flores")
    mostrar_menu()
