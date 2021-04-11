import hashlib
from datetime import datetime

class Block():
    def __init__(self, prevHash, transaction):
        self.prevHash = prevHash
        self.transaction = transaction
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def hash(self):
        hash = hashlib.sha256()
        hash.update(' '.join([str(e) for e in self.__dict__]).encode())
        return hash.hexdigest()