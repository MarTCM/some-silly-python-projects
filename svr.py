import socket
import os


#host_name = socket.gethostname()
#host_ip = socket.gethostbyname(host_name)
#print("Hostname :  ", host_name)
#print("IP : ", host_ip)

host_ip = '192.168.1.28'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host_ip, 4444))
s.listen()


def server():
    while True:
        print("Listening on port 4444...")
        clientsocket, address = s.accept()
        print(f"\u001b[32;1mConnection from {address} has been established.\u001b[37m")
        while True:
            try:
                chat = input("\u001b[33m>\u001b[37m")
                if chat == "shutdown":
                    clientsocket.send(bytes(str(os.system("shutdown /s")), "utf-8"))
                elif chat != "error":
                    clientsocket.send(bytes(str(chat), "utf-8"))
            except ConnectionResetError:
                print("Connection Lost!")
                break
                server()





