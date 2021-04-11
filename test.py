import Block,Chain,Transaction,Wallet

a = Wallet.Wallet()
b = Wallet.Wallet()
c = Wallet.Wallet()

a.send(b.publicKey, 10000)

print()