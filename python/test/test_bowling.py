from unittest import TestCase

from bowling import Bowling


class TestBowling(TestCase):

    def roll_n_time_pins(self, rolls, pins):
        for i in range(rolls):
            self.bowling.roll(pins)

    def setUp(self) -> None:
        self.bowling = Bowling()

    def test_all_zero_is_0(self):
        self.roll_n_time_pins(20, 0)
        self.assertEqual(0, self.bowling.score())

    def test_all_one_is_20(self):
        self.roll_n_time_pins(20, 1)
        self.assertEqual(20, self.bowling.score())

    def test_all_strike_is_300(self):
        self.roll_n_time_pins(12, 10)
        self.assertEqual(300, self.bowling.score())

    def test_no_bonus(self):
        self.bowling.roll(1)
        self.bowling.roll(4)
        self.assertEqual(5, self.bowling.score())

    def test_spare(self):
        self.bowling.roll(6)
        self.bowling.roll(4)
        self.bowling.roll(3)
        self.assertEqual(6 + 4 + 3 + 3, self.bowling.score())

    def test_strike(self):
        self.bowling.roll(10)
        self.bowling.roll(4)
        self.bowling.roll(3)
        self.assertEqual(10 + 4 + 3 + 3, self.bowling.score())

    def test_given_game(self):
        rolls = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
        for roll in rolls:
            self.bowling.roll(roll)

        self.assertEqual(133, self.bowling.score())
