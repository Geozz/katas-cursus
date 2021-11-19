class Diseur:
    def suivant(self, current: str):
        previous_char = None
        count_pc = 0
        result = ""

        for char in current:
            if char == previous_char:
                count_pc += 1
            else:
                if previous_char:
                    result += self.construct_next(count_pc, previous_char)
                previous_char = char
                count_pc = 1

        result += self.construct_next(count_pc, previous_char)

        return result

    def construct_next(self, count_pc, previous_char):
        return str(count_pc) + previous_char
