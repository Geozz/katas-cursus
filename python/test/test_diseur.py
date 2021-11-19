from unittest import TestCase

from diseur import Diseur


class TestDiseur(TestCase):
    
    def setUp(self) -> None:
        self.diseur = Diseur()

    def test_1(self):
        self.assertEqual("11", self.diseur.suivant("1"))

    def test_11(self):
        self.assertEqual("21", self.diseur.suivant("11"))

    def test_21(self):
        self.assertEqual("1211", self.diseur.suivant("21"))

    def test_1211(self):
        self.assertEqual("111221", self.diseur.suivant("1211"))

    def test_111221(self):
        self.assertEqual("312211", self.diseur.suivant("111221"))

    def test_312211(self):
        self.assertEqual("13112221", self.diseur.suivant("312211"))
