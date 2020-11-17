from socket import *

host = ''
port = 6666
buffer_size = 1024
address = (host,port)
# serverSocket是欢迎套接字，它负责与客户端套接字进行三次握手建立连接
serverSocket = socket(AF_INET, SOCK_STREAM)
# 将端口号与套接字绑定
serverSocket.bind(address)
# 建立连接后套接字处于监听状态
serverSocket.listen(1)
print('The server is ready to receive...')
while True:
    # connectSocket为客户端的连接套接字，由这个特定的客户专用
    connectSocket, addr = serverSocket.accept()
    data = connectSocket.recv(buffer_size)
    message = data.decode().upper()
    connectSocket.send(message.encode())
    connectSocket.close()
