from socket import *

host = '192.168.31.81'
port = 6666
buffer_size = 1024
address = (host,port)

clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(), (host, port))
modifiedMessage, addr = clientSocket.recvfrom(buffer_size)
print(modifiedMessage.decode())
clientSocket.close()
