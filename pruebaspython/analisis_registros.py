# Diccionario para almacenar los intentos fallidos por IP
intentos_fallidos = {}

# Contador de intentos exitosos
intentos_exitosos = 0

# Leer el archivo de registro
try:
    with open("registro.txt", "r") as archivo:

        for linea in archivo:
            datos = linea.split()

            if len(datos) == 3:
                ip = datos[0]
                estado = datos[2]

                if estado == "OK":
                    intentos_exitosos += 1

                elif estado == "FAILED":
                    if ip in intentos_fallidos:
                        intentos_fallidos[ip] += 1
                    else:
                        intentos_fallidos[ip] = 1

    # Mostrar resultados
    print("\n===== ANÁLISIS DE REGISTROS =====")

    print("\nIntentos exitosos:", intentos_exitosos)

    print("\nIntentos fallidos por IP:")

    for ip, cantidad in intentos_fallidos.items():
        print(ip, ":", cantidad)

    # Detectar IP sospechosas
    print("\nDirecciones IP sospechosas (más de 3 fallos):")

    sospechosas = False

    for ip, cantidad in intentos_fallidos.items():
        if cantidad > 3:
            print(ip, ":", cantidad, "intentos fallidos")
            sospechosas = True

    if not sospechosas:
        print("No se han detectado IP sospechosas.")

except FileNotFoundError:
    print("Error: No se encuentra el archivo registro.txt.")
