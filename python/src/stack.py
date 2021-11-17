class Stack:
    def __init__(self):
        self.value = []

    def push(self, value):
        self.value.append(value)

    def pop(self):
        return self.value.pop()

    def count(self):
        return len(self.value)
