from unittest import TestCase

from cart import Cart


class TestCart(TestCase):

    def setUp(self) -> None:
        self.cart = Cart()

    def test_empty_cart_price_is_0(self):
        self.assertEqual(0, self.cart.get_price())

    def test_one_book_is_8(self):
        self.cart.add_book("À l’école des sorciers")
        self.assertEqual(8, self.cart.get_price())

    def test_two_diff_books_apply_5discount(self):
        self.cart.add_book("À l’école des sorciers")
        self.cart.add_book("La Chambre des secrets")
        self.assertEqual(8 * 2 * 0.95, self.cart.get_price())

    def test_3_diff_books_apply_10discount(self):
        self.cart.add_book("À l’école des sorciers")
        self.cart.add_book("La Chambre des secrets")
        self.cart.add_book("Le Prisonnier d'Azkaban")
        self.assertEqual(8 * 3 * 0.90, self.cart.get_price())

    def test_same_book_no_reduction(self):
        self.cart.add_book("À l’école des sorciers")
        self.cart.add_book("À l’école des sorciers")
        self.assertEqual(8 * 2, self.cart.get_price())

    def test_5_diff_books_with_lots(self):
        self.cart.add_book("À l’école des sorciers")
        self.cart.add_book("La Chambre des secrets")
        self.cart.add_book("Le Prisonnier d'Azkaban")

        self.cart.add_book("À l’école des sorciers")
        self.cart.add_book("La Chambre des secrets")

        self.assertEqual(8 * 3 * 0.90 + 8 * 2 * 0.95, self.cart.get_price())
