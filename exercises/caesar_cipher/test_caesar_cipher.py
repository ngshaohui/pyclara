import unittest
from caesar_cipher_sol import encrypt_text


class TestStringMethods(unittest.TestCase):
    def test_0_with_space(self):
        self.assertEqual(encrypt_text("bananas and apples", 0), "bananas and apples")

    def test_1(self):
        self.assertEqual(encrypt_text("xyzabc", 1), "yzabcd")

    def test_2(self):
        self.assertEqual(encrypt_text("zebra", 2), "bgdtc")

    def test_6_with_capital_and_space(self):
        self.assertEqual(encrypt_text("Hello world", 6), "Nkrru cuxrj")

    def test_26_with_capital(self):
        self.assertEqual(encrypt_text("Constantinople", 26), "Constantinople")

    def test_27(self):
        self.assertEqual(encrypt_text("yahoo", 27), "zbipp")

    def test_27_with_capital(self):
        self.assertEqual(encrypt_text("AMAZON", 27), "BNBAPO")

    def test_52_with_capital_and_space(self):
        self.assertEqual(encrypt_text("Cookies aNd creaM", 52), "Cookies aNd creaM")

    def test_77_with_capital_and_space(self):
        self.assertEqual(encrypt_text("Bacon and eggs", 77), "Azbnm zmc dffr")

    def test_negative_1(self):
        self.assertEqual(encrypt_text("yzabcd", -1), "xyzabc")

    def test_negative_26_with_space(self):
        self.assertEqual(encrypt_text("gula melaka", -26), "gula melaka")

    def test_negative_33_with_capital_and_space(self):
        self.assertEqual(encrypt_text("Nature Valley CRUNCHY GraNolA BarS", -33), "Gtmnkx Oteexr VKNGVAR ZktGheT UtkL")


if __name__ == '__main__':
    unittest.main()
