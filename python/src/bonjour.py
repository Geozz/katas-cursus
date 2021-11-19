from datetime import time


class Bonjour:
    def __init__(self, clock: time):
        self.clock = clock

    def greet(self, first_name: str):
        stripped_name = first_name.strip()
        capitalized_name = stripped_name.capitalize()

        if 6 <= self.clock.hour < 18:
            salutation = "Bonjour "
        elif 18 <= self.clock.hour <= 23:
            salutation = "Bonsoir "
        else:
            salutation = "Bonne nuit "

        return salutation + capitalized_name
