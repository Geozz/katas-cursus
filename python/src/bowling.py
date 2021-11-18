class Bowling:

    def __init__(self):
        self._score = []

    def roll(self, pins):
        self._score.append(pins)

    def score(self):
        result = 0
        for idx, score in enumerate(self._score):
            result += score

            if score == 10:
                result += self._score[idx + 1]
                result += self._score[idx + 2]

        return result
