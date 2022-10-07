from TechProduct import TechProduct


class Product:
    type = "Product"

    def __init__(self, id=0, name="", description="", type=None, price=0.0):
        self.name = name
        self.description = description
        self.type = type
        self.price = price
        self.id = id

    def __str__(self):
        return str(self.id) + "," + self.name + ", " + self.description + "," + str(self.type) + "," + str(self.price)
