class Cart:
    def __init__(self):
        self.books = [[]]

    def add_book(self, title):
        for lot in self.books:
            if title in lot:
                continue
            lot.append(title)
            return

        self.books.append([title])

    def get_price(self):
        result = 0
        for lot in self.books:
            discount = (len(lot) - 1) * 0.05
            result += 8 * len(lot) * (1 - discount)
        return result
