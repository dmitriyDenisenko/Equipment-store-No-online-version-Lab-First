class ProductNotExist(Exception):
    def __int__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("Product Not Exist: ")
        if self.message:
            return self.message
