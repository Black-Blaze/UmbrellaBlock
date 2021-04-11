from Crypto.PublicKey import RSA
import hashlib,hmac, Transaction, Chain

class Wallet():
    def __init__(self):
        key = RSA.generate(1024)
        self.publicKey = key.exportKey('PEM')
        self.privateKey = key.publickey().exportKey('PEM')
        print(self.privateKey)

    def send(self, reciever, value):
        tr = Transaction.Transaction(self.publicKey, reciever, value)
        sign = hmac.new(self.privateKey, b"cont", hashlib.sha256).hexdigest()
        print(sign)
        Chain.Chain().addblock(tr, self.publicKey, sign)

Wallet().send("aaaa","aaaa")