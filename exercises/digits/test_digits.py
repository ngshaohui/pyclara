import unittest
from digits import sum_digits


class TestStringMethods(unittest.TestCase):

    def test_1933091(self):
        self.assertEqual(sum_digits(1933091), 26)

    def test_0(self):
        self.assertEqual(sum_digits(0), 0)

    def test_1(self):
        self.assertEqual(sum_digits(1), 1)

    def test_10(self):
        self.assertEqual(sum_digits(10), 1)

    def test_11011(self):
        self.assertEqual(sum_digits(11011), 4)

    def test_34120(self):
        self.assertEqual(sum_digits(34120), 10)

    def test_9999(self):
        self.assertEqual(sum_digits(9999), 36)

    def test_9988(self):
        self.assertEqual(sum_digits(9988), 34)


if __name__ == '__main__':
    unittest.main()
