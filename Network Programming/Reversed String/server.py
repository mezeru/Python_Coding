import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.bind((host, port))

s.listen(2)

client, addrs = s.accept()

print("Got connected with ", addrs)

msg = client.recv(1024)
msg = msg.decode("utf-8")
msg = msg[::-1]

client.send(str(msg).encode("utf-8"))

s.close()
