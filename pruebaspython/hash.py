"""
Crea un programa en Python que te permita ingresar texto y generar su hash SHA-256.

Añade a tu programa una función para generar el hash SHA-256 de un archivo.
"""

import hashlib


# Función para generar el hash SHA-256 de un texto
def hash_texto():
    texto = input("Introduce el texto: ")

    hash_sha256 = hashlib.sha256(texto.encode("utf-8")).hexdigest()

    print("\nHash SHA-256 del texto:")
    print(hash_sha256)


# Función para generar el hash SHA-256 de un archivo
def hash_archivo():
    ruta = input("Introduce la ruta del archivo: ")

    try:
        sha256 = hashlib.sha256()

        with open(ruta, "rb") as archivo:
            while bloque := archivo.read(4096):
                sha256.update(bloque)

        print("\nHash SHA-256 del archivo:")
        print(sha256.hexdigest())

    except FileNotFoundError:
        print("Error: El archivo no existe.")

    except PermissionError:
        print("Error: No tienes permisos para acceder al archivo.")


# Menú principal
def menu():
    while True:
        print("\n===== GENERADOR DE HASH SHA-256 =====")
        print("1. Generar hash de un texto")
        print("2. Generar hash de un archivo")
        print("3. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            hash_texto()

        elif opcion == "2":
            hash_archivo()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecutar programa
menu()
