"""
Crea un programa en Python que resuelva el desafío FizzBuzz, donde habrá una función que reciba un número como parámetro y devuelva "fizz" para valores divisibles por 3, "buzz" para valores divisibles por 5, y "fizz buzz" para valores divisibles por 3 y 5 al mismo tiempo.

"""


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
