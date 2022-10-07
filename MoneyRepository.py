class MoneyRepository:
    type = "MoneyRepository"

    def __init__(self, bank = 0):
        self.bank = bank

    def make_deal(self, count):
        self.bank += count
