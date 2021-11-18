class Roman:
    def decode(self, roman_number: str):
        result = 0
        next_value = 0
        for char in roman_number[::-1]:
            current_value = self.decode_single_char(char)
            if next_value > current_value:
                result -= current_value
            else:
                result += current_value
            next_value = current_value
        return result

    @staticmethod
    def decode_single_char(roman_number):
        if 'I' == roman_number:
            return 1
        if 'V' == roman_number:
            return 5
        if 'X' == roman_number:
            return 10
        if 'L' == roman_number:
            return 50
        if 'C' == roman_number:
            return 100
        if 'D' == roman_number:
            return 500
        if 'M' == roman_number:
            return 1000
        return 0
