import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9999
host = socket.gethostname()

s.connect((host, port))
msg = input().encode("utf-8")
s.send(msg)

s.close()
