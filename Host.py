import socket
import multiprocessing

clientHost = ("0.0.0.0", 8000) #Host At 0.0.0.0 To Allow Remote Connections. 8000 Is Default For Clients.
clientSocket = socket.socket(socket.AF_INET) #Create Socket For Clients
clientSocket.bind(clientHost) #Attach Socket For Clients
clientSocket.listen(5) #Listen On Client Socket

minerHost = ("0.0.0.0", 1600) #Host At 0.0.0.0 To Allow Remote Connections. 1600 Is Default For Miners.
minerSocket = socket.socket(socket.AF_INET) #Create Socket For Miners
minerSocket.bind(minerHost) #Attach Socket For Miners
minerSocket.listen(5) #Listen On Miner Socket

def handleClient(sock):
    pass

def handleMiner(sock):
    pass


def acceptMiners():
    while True:
        currMiner = clientSocket.accept()
        p = multiprocessing.Process(target=handleMiner, args=(currMiner,))
        p.start()
        p.join()

minerListener = multiprocessing.Process(target=acceptMiners)

while True:
    currClient = clientSocket.accept()
    p = multiprocessing.Process(target=handleClient, args=(currClient,))
    p.start()
    p.join()