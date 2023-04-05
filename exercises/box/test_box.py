import unittest
from box import get_surface_area


class TestStringMethods(unittest.TestCase):

    def test_12_3_10(self):
        self.assertEqual(get_surface_area(12, 3, 10), 372)

    def test_10_20_30(self):
        self.assertEqual(get_surface_area(10, 20, 30), 2200)

    def test_200_1_300(self):
        self.assertEqual(get_surface_area(200, 1, 300), 121000)


if __name__ == '__main__':
    unittest.main()
