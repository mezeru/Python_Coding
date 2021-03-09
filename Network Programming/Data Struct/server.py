import socket
import sys


class DATA:
    def __init__(self, vardata, ip):
        self.ip = ip
        self.vardata = vardata
        self.sizeData = sys.getsizeof(vardata)


if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 9999
    host = socket.gethostname()
    s.bind((host, port))
    s.listen()
    client, addrs = s.accept()

    msg = client.recv(1024).decode("Utf-8")
    c1 = DATA(msg, socket.gethostbyname(addrs[0]))

    print("Size of Data : ", c1.sizeData,
          "\nIP : ", c1.ip, "\nData : ", c1.vardata)

    s.close()
