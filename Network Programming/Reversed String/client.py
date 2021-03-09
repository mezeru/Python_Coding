import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

s.connect((host, port))

msg = input()
s.send(msg.encode("utf-8"))

msg = s.recv(1024)

print("The reverse string  is ", str(msg))
