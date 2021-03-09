import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
host = socket.gethostname()
port = 9999

s.connect((host, port))

msg = input()

s.sendto(msg.encode("utf-8"), (host, port))

try:
    msg, addrs = s.recvfrom(1024)
    print(msg.decode("utf-8"))

except:
    print("MSg not received")


s.close()
