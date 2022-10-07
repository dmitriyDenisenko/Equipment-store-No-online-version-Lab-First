class InsufficientFundsError(Exception):
    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = None

    def __str__(self):
        print("There is no money on the account to buy")
