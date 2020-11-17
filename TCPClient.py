from socket import *

host = '192.168.31.81'
port = 6666
buffer_size = 1024
address = (host,port)
# 创建套接字，SOCK_STREAM指示是个TCP套接字
clientSocket = socket(AF_INET,SOCK_STREAM)
# 创建TCP连接，执行三次握手
clientSocket.connect(address)
message = input("Input lowercase sentence:")
# 发送数据时不需要附上目标地址（用的是send方法），因为共用一个连接
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(buffer_size)
print('From Server: ', modifiedMessage.decode())
clientSocket.close()
