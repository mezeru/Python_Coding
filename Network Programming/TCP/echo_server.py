import socket
import sys

s = socket.socket()

localhost = '127.0.0.1'
port = 8882

s.bind((localhost,port))
s.listen()

print("Waiting for Connection")

client,address = s.accept()

print("Connection established from ",address)


conn = True

while conn:
    data = client.recv(1024)
    msg  = data.decode("utf-8")
    print(msg)
    client.send(data)


    if(msg == "quit"):
        break

