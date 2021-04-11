class Transaction():
    def __init__(self, sender, reciever, value):
        self.sender = sender
        self.reciever = reciever
        self.value = value

    def string(self):
        return ' '.join([str(e) for e in self.__dict__])