import pytest

from mayor_numero import mayor_numero

""""
class TestMayorNumero(unittest.TestCase):
    def test_mayor_numero(self):
        self.assertEqual(mayor_numero(3, 5, 2), 5)
        self.assertEqual(mayor_numero(10, 7, 15), 15)
        self.assertEqual(mayor_numero(1, 1, 1), 1)
        self.assertEqual(mayor_numero(-5, -7, -4), -2)


if __name__ == "__main__":
    unittest.main()
    """

"""
test con pytest


"""


@pytest.mark.parametrize(
    "a, b, c, expected", [(3, 5, 2, 5), (10, 7, 15, 15), (1, 1, 1, 1), (-5, -7, -4, -4)]
)
def test_mayor_numero(a, b, c, expected):
    assert mayor_numero(a, b, c) == expected
