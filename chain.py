from bloc import Bloc
import requests

class Chain:

    def __init__(self, number_of_transactions_per_bloc):
        self.chain = []
        genesis = Bloc(0, 0)
        genesis.proofOfWork()
        self.number_of_transactions_per_bloc = number_of_transactions_per_bloc
        self.chain.append(genesis)
        print("init chain")

    def getLength(self):
        return len(self.chain)

    def getBloc(self, index):
        return self.chain[index]

    def getLastBloc(self):
        return self.getBloc(self.getLength()-1)

    def mine(self, bloc=None):
        newBloc = Bloc(self.getLength(), self.getLastBloc().hash()) if bloc is None else bloc
        if bloc.previousBlocHash == None:
            bloc.previousBlocHash = self.getLastBloc().hash()
        newBloc.proofOfWork()
        self.chain.append(newBloc)
        self.nodes = []

    def addNode(self, newNode):
        if newNode not in self.nodes:
            self.nodes.append(newNode)

     # This will return the Chain in a JSON format
    def __str__(self):
        return "{" + \
                ",".join([f"\"{x.index}\": {str(x)}" for x in self.chain]) + \
                "}\n"

    def consensus(self):
        for node in self.nodes:
            r = requests.get(node + "/chain")
            if r.status_code == 200:
                chain = r.json()
                if len(chain) > self.getLength():
                    self.chain = []
                    for bloc in chain:
                        newBloc = chain[bloc]
                        self.chain.append(Bloc(newBloc['index'],
                                               newBloc['lastHash'],
                                               newBloc['timestamp'],
                                               newBloc['proof']))
