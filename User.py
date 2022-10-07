from ProductsRepository import ProductsRepository
from Product import Product
from TechProduct import TechProduct
from UserBankError import UserBankError


class User:
    type = "User"

    def __init__(self, bank=0, products=[], sum_of_by=0):
        self.bank = bank
        self.products = products
        self.sum_of_buy = float(sum_of_by)

    def add_product(self, id, product_rep):
        product = product_rep.get_product_by_id(id)
        self.products.append(product)
        self.sum_of_buy += product.price

    def make_buy(self, money_rep):
        if self.bank - self.sum_of_buy >= 0:
            money_rep.make_deal(self.sum_of_buy)
            self.bank -= self.sum_of_buy
            self.sum_of_buy = 0
            self.products = []
        else:
            raise UserBankError("Not enough money to buy")

    def remove_product(self, id, product_rep):
        product = product_rep.find_product_by_id(id)
        if product in self.products:
            self.products.remove(product)
            product_rep.put_product_back(product)
        else:
            raise UserBankError("You can put back u pants!!!")

    def get_bank(self):
        return self.bank
