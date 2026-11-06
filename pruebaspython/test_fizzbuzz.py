import unittest
from fizzbuzzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), "fizz")
        self.assertEqual(fizz_buzz(5), "buzz")
        self.assertEqual(fizz_buzz(15), "fizz buzz")


if __name__ == "__main__":
    unittest.main()
