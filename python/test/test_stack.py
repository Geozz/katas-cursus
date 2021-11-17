from unittest import TestCase

from stack import Stack


class TestStack(TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_push_stack_provided_value(self):
        self.stack.push(42)
        self.assertEqual(42, self.stack.pop())

    def test_push_stack_FILO(self):
        self.stack.push(42)
        self.stack.push(69)
        self.assertEqual(69, self.stack.pop())
        self.assertEqual(42, self.stack.pop())

    def test_count(self):
        self.stack.push(42)
        self.assertEqual(1, self.stack.count())
        self.stack.push(69)
        self.assertEqual(2, self.stack.count())
