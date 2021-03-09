import socket
import sys

client = socket.socket()

localhost = '127.0.0.1'
port = 8882

client.connect((localhost,port))

conn = True


while conn:
    msg = input("Enter the msg: ")
    data = msg.encode("utf-8")
    client.send(data)

    data_rec = client.recv(1024)
    msg_recv = data_rec.decode("utf-8")
    print("Server says")
    print(msg_recv)

    if(msg_recv == "quit"):
        break
