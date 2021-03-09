import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

host = socket.gethostname()
port = 3545

s.connect((host, port))

msg = "This is a msg from server"
msg = msg.encode("Utf-8")

s.sendto(msg, (host, port))

data, addrs = s.recvfrom(1024)

print(str(data))

s.close()
