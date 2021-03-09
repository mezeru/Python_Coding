import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

host = socket.gethostname()
port = 9999

s.bind((host, port))

msg, addrs = s.recvfrom(1024)
msg = msg.decode("utf-8")
msg = int(msg)
msg = msg*msg

msg = str(msg).encode("utf-8")

s.sendto(msg, addrs)

s.close()
