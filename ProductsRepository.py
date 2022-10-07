from ProductNotExist import ProductNotExist
from Product import Product
from TechProduct import TechProduct


class ProductsRepository:
    type = "ProductsRepository"
    products_DTO = {}

    def __init__(self, products=[]):
        self.all_products = products
        self.generate_DTO_products()

    def get_product_by_id(self, id):
        for product in self.products_DTO.keys():
            if product == id:
                if self.products_DTO[product] > 0:
                    change_products = self.products_DTO[product]
                    change_products -= 1
                    self.products_DTO[product] = change_products
                    self.all_products.remove(self.find_product_by_id(id))
                    return self.find_product_by_id(id)
                else:
                    raise ProductNotExist("Product is out of stock")
        raise ProductNotExist("We do not have such products")

    def find_product_by_id(self, id):
        for prod in self.all_products:
            if prod.id == id:
                return prod
        else:
            raise ProductNotExist("its error by not in products")

    def put_product_back(self, product):
        if self.find_product_by_id(product.id):
            change_products = self.products_DTO[product.id]
            change_products += 1
            self.products_DTO[product.id] = change_products
            self.all_products.append(product)
        else:
            ProductNotExist("You're trying to put in a product we didn't have! Thank you! But no")

    def get_products_DTO(self):
        return self.products_DTO

    def generate_DTO_products(self):
        for product in self.all_products:
            if product not in self.products_DTO:
                count = 0
                for i in self.all_products:
                    if int(product.id) == int(i.id):
                        count += 1
                self.products_DTO[product.id] = count

    def add_product(self, product):
        self.all_products.append(product)
        self.generate_DTO_products()

    def print_products_having(self):
        for id in self.products_DTO:
            print(id + ": " + self.find_product_by_id(id) + ". We have: " + self.products_DTO[id])

    def desireal_products(self):
        product_new = []
        for product in self.all_products:
            product_split = product.split(",")
            product_new.append(Product(int(product_split[0]), product_split[1], product_split[2], self.add_type(product_split[3]), float(product_split[4])))
        self.all_products = product_new
        self.generate_DTO_products()

    def add_type(self, line):
        if line == "TechProduct.LIFE_TECHNIQUE":
            return TechProduct.LIFE_TECHNIQUE
        elif line == "TechProduct.PHONES":
            return TechProduct.PHONES
        elif line == "TechProduct.TVS":
            return TechProduct.TVS
        elif line == "TechProduct.COMPUTERS":
            return  TechProduct.COMPUTERS
        elif line == "TechProduct.OFFIC":
            return TechProduct.OFFICE
        elif line == "TechProduct.LEISURE":
            return TechProduct.LEISURE
        elif line == "TechProduct.INSTRUMENT":
            return TechProduct.INSTRUMENT
        elif line == "TechProduct.CONSTRUCTION":
            return TechProduct.CONSTRUCTION
        elif line == "TechProduct.HOUSEHOLD_PRODUCTS":
            return TechProduct.HOUSEHOLD_PRODUCTS
        elif line == "TechProduct.AUTO_PRODUCTS":
            return TechProduct.AUTO_PRODUCTS
        elif line == "TechProduct.ACCESSORIES":
            return TechProduct.ACCESSORIES