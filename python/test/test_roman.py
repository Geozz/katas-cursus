from unittest import TestCase

from roman import Roman


class TestRoman(TestCase):
    def setUp(self) -> None:
        self.roman = Roman()

    def test_448(self):
        self.assertEqual(448, self.roman.decode("CDXLVIII"))

    def test_1998(self):
        self.assertEqual(1998, self.roman.decode("MCMXCVIII"))

    def test_1(self):
        self.assertEqual(1, self.roman.decode("I"))

    def test_5(self):
        self.assertEqual(5, self.roman.decode("V"))

    def test_10(self):
        self.assertEqual(10, self.roman.decode("X"))

    def test_50(self):
        self.assertEqual(50, self.roman.decode("L"))

    def test_100(self):
        self.assertEqual(100, self.roman.decode("C"))

    def test_500(self):
        self.assertEqual(500, self.roman.decode("D"))

    def test_1000(self):
        self.assertEqual(1000, self.roman.decode("M"))

    def test_2(self):
        self.assertEqual(2, self.roman.decode("II"))

    def test_4(self):
        self.assertEqual(4, self.roman.decode("IV"))
