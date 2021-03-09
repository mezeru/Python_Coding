import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 4383

s.connect((host, port))

msg = "Hello\nWorld\nI\nam\nHere\nThis is Client\n"

s.send(msg.encode("Utf-8"))

s.close()
