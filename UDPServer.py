from socket import *

host = ''
port = 6666
buffer_size = 1024
address = (host,port)

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(address)
print('The server is ready to receive...')
while True:
    data, addr = serverSocket.recvfrom(buffer_size)
    message = data.decode().upper()
    serverSocket.sendto(message.encode(), addr)
