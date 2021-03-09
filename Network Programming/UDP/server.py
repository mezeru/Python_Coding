import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

host = socket.gethostname()
port = 3545

s.bind((host, port))

data, addrs = s.recvfrom(1024)

print("Server has connectedd to ", addrs)

print(data.decode("Utf-8"))

msg = "This is message from server"
msg = msg.encode("Utf-8")

s.sendto(msg, addrs)

s.close()
