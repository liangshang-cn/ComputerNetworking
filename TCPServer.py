from socket import *

host = ''
port = 6666
buffer_size = 1024
address = (host,port)

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(address)
serverSocket.listen(1)
print('The server is ready to receive...')
while True:
    connectSocket, addr = serverSocket.accept()
    data = connectSocket.recv(buffer_size)
    message = data.decode().upper()
    connectSocket.send(message.encode())
    connectSocket.close()
