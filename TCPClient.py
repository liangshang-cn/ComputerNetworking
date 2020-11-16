from socket import *

host = '192.168.31.81'
port = 6666
buffer_size = 1024
address = (host,port)

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.connect(address)
message = input("Input lowercase sentence:")
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(buffer_size)
print('From Server: ', modifiedMessage.decode())
clientSocket.close()
