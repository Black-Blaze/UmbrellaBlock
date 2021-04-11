import socket

host = ("0.0.0.0", 80) #Host At 0.0.0.0 To Allow Remote Connections. 80 Is Default For Client.
clientSocket = socket.socket(socket.AF_INET) #Create Socket
clientSocket.bind(host) #Attach Socket