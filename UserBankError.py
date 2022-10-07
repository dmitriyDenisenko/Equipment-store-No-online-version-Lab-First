class UserBankError(Exception):
    def __int__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("User bank error: ")
        if self.message:
            return self.message
