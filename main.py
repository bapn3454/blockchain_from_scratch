from bloc import Bloc
from chain import Chain
from transaction import Transaction

demo = Chain(5)
transactions = open('transactions.txt').readlines()
transaction_array = []
bloc = None
for line in transactions:
    row = line.split(',')
    index, amount, sender, receiver = [i.strip() for i in row]
    if int(index) % 5 == 0:
        bloc = Bloc(int(index)/5)
    t = Transaction(int(index), amount, sender, receiver)
    print(bloc)
    print("index = {}, amount = {}, sender = {}, receiver = {}".format(t.index, t.amount, t.sender, t.receiver))
    bloc.addTransaction(t)
    if int(index) % 5 == 4:
        if bloc != None:
            demo.mine(bloc)

print(demo)

# TODO corriger le __str__ de transaction pour garder un format json correct
#       >peut etre qu'on doit l'enregistrer en string, puis creer des fonctions pour caster