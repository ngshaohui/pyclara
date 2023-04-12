import unittest
from candles import count_candles


class TestStringMethods(unittest.TestCase):

    def test_9_5(self):
        self.assertEqual(count_candles(9, 5), 11)

    def test_0_0(self):
        self.assertEqual(count_candles(0, 0), 0)

    def test_5_3(self):
        self.assertEqual(count_candles(5, 3), 7)

    def test_100_7(self):
        self.assertEqual(count_candles(100, 7), 116)

    def test_10_11(self):
        self.assertEqual(count_candles(10, 11), 10)

    def test_10_10(self):
        self.assertEqual(count_candles(10, 10), 11)

    def test_123_12(self):
        self.assertEqual(count_candles(123, 12), 134)

    def test_80_81(self):
        self.assertEqual(count_candles(80, 81), 80)

    def test_3333_3(self):
        self.assertEqual(count_candles(3333, 3), 4999)

    def test_3333_2(self):
        self.assertEqual(count_candles(3333, 2), 6665)

    def test_99999_18(self):
        self.assertEqual(count_candles(99999, 18), 105881)

    def test_1_10000(self):
        self.assertEqual(count_candles(1, 10000), 1)


if __name__ == '__main__':
    unittest.main()
