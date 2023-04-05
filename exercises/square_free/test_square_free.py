import unittest
from square_free import count_square_free


class TestStringMethods(unittest.TestCase):

    def test_1_10(self):
        self.assertEqual(count_square_free(1, 10), 7)

    def test_1_5(self):
        self.assertEqual(count_square_free(1, 5), 4)

    def test_132_157(self):
        self.assertEqual(count_square_free(132, 157), 15)

    def test_2_10(self):
        self.assertEqual(count_square_free(2, 10), 6)

    def test_1_2(self):
        self.assertEqual(count_square_free(1, 2), 2)

    def test_8_9(self):
        self.assertEqual(count_square_free(8, 9), 0)

    def test_3000_50000(self):
        self.assertEqual(count_square_free(3000, 50000), 28577)

    def test_1_11(self):
        self.assertEqual(count_square_free(1, 11), 8)

    def test_55_88(self):
        self.assertEqual(count_square_free(55, 88), 22)

    def test_2034_2173(self):
        self.assertEqual(count_square_free(2034, 2173), 85)

    def test_864_2132(self):
        self.assertEqual(count_square_free(864, 2132), 771)


if __name__ == '__main__':
    unittest.main()
