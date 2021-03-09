import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4383

s.bind((host, port))

s.listen()

client, addrs = s.accept()

print("connected to ", addrs)

msg = client.recv(1024)
msg = msg.decode("Utf-8")


if "\n" in msg:
    for i in msg:
        print(i, end="")
