"""
Crea un programa Python que comprobe a fortaleza de contrasinais.
Como mínimo debe comprobar que contén:
mínimo 8 caracteres.
maiúsculas e minúsculas
números
caracteres especiais
Debe mostrar un resumo das comprobacións que non se cumpran.
"""

contraseña = input("Introduce una contraseña ")


def comprobar_contraseña(contraseña):
    errores = []
    if len(contraseña) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    if not any(c.isupper() for c in contraseña):
        errores.append("La contraseña debe tener al menos una letra mayúscula.")
    if not any(c.islower() for c in contraseña):
        errores.append("La contraseña debe tener al menos una letra minúscula.")
    if not any(c.isdigit() for c in contraseña):
        errores.append("La contraseña debe tener al menos un número.")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in contraseña):
        errores.append("La contraseña debe tener al menos un carácter especial.")

    return errores


errores = comprobar_contraseña(contraseña)
if errores:
    print("Error en la contraseña:")
    for error in errores:
        print(f" - {error}")
else:
    print("La contraseña es fuerte.")
