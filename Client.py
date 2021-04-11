import socket

s = socket.socket(socket.AF_INET)
s.connect(("0.0.0.0",8000))
while True:
    try:
        s.send(input(">>>").encode())
    except:
        print("Please Try Again")
        s.connect(("0.0.0.0",8000))