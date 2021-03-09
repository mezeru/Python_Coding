import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.connect((host, port))

msg = input()
s.send(msg.encode("utf-8"))

msg1 = s.recv(1024)

print("The message is ", msg, "number of bytes read is ", str(msg1))
