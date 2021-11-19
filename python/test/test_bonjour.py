from datetime import time
from unittest import TestCase

from bonjour import Bonjour


class TestBonjour(TestCase):

    def setUp(self) -> None:
        self.bonjour = Bonjour(time(15, 35))

    def test_say_bonjour(self):
        self.assertEqual("Bonjour Geoffrey", self.bonjour.greet("Geoffrey"))

    def test_trim(self):
        self.assertEqual("Bonjour Geoffrey", self.bonjour.greet(" Geoffrey "))

    def test_capitalize(self):
        self.assertEqual("Bonjour Geoffrey", self.bonjour.greet("geoffrey"))

    def test_soir(self):
        bonjour = Bonjour(time(20, 50))
        self.assertEqual("Bonsoir Geoffrey", bonjour.greet("Geoffrey"))

    def test_nuit(self):
        bonjour = Bonjour(time(1, 24))
        self.assertEqual("Bonne nuit Geoffrey", bonjour.greet("Geoffrey"))
