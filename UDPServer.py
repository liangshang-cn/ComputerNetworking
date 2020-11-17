from socket import *

host = ''
port = 6666
buffer_size = 1024
address = (host,port)
# 创建服务端的套接字
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 通过绑定，显式地为套接字分配一个端口号
serverSocket.bind(address)
print('The server is ready to receive...')
while True:
    data, addr = serverSocket.recvfrom(buffer_size)
    message = data.decode().upper()
    serverSocket.sendto(message.encode(), addr)
