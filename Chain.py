import Block, Transaction, hashlib, hmac

class Chain():
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.chain = [Block.Block(None, Transaction.Transaction("Sushant", "a", 1000))]

    def getlastblock(self):
        return self.chain[-1]

    def addblock(self, transaction, senderKey, signature):
        if(hmac.compare_digest(senderKey, signature.encode())):
            nBlock = Block(self.getlastblock().hash(), transaction)
            self.chain.append(nBlock)