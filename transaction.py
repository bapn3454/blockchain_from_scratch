class Transaction:

    def __init__(self, index, amount, sender, receiver):
        self.index = index
        self.amount = amount
        self.sender = sender
        self.receiver = receiver

    def __str__(self):
        return str(self.__dict__)#.replace("'",'"')