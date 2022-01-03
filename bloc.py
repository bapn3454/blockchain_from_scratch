import hashlib
import random
import time

class Bloc:

    def __init__(self, index, previous_bloc_hash=None, timestamp=None,  proof=None):
        self.index = index
        self.previousBlocHash = previous_bloc_hash
        self.creationTimestamp = int(time.time()) if timestamp is None else timestamp
        self.transactions = []
        self.proof = 0 if proof is None else proof
        print("init bloc")

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def hash(self):
        return hashlib.sha256(str(self.__dict__).encode("utf-8")).hexdigest()

    def proofOfWork(self):
        while self.hash()[-5:] != "00000":
            self.proof += random.randint(1,10)

    # This will return The Bloc in a JSON format
    def __str__(self):
        return str(self.__dict__).replace("'",'"')