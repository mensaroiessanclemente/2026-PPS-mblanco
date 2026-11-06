import pytest
from calculadora import sumar, restar, multiplicar, dividir

# def test_sumar():
# assert sumar(2, 3) == 5


# def test_suma_negativos():
# assert sumar(-2, -3) == -5


@pytest.mark.parametrize(
    "a, b, resultado_esperado",
    [
        (2, 3, 5),
        (5, 5, 10),
        (-2, -3, -5),
        (10, 0, 10),
    ],
)
def test_sumar(a, b, resultado_esperado):
    assert sumar(a, b) == resultado_esperado
