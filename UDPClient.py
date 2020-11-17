from socket import *

host = '192.168.31.81'
port = 6666
buffer_size = 1024
address = (host,port)

# 创建客户端的套接字，参数AF_INET表示IPv4，SOCK_DGRAM表示是个UDP套接字
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode(), (host, port))
# 输入时字节流通过encode编码为字符串，输出时字符串通过decode解码为字节
modifiedMessage, addr = clientSocket.recvfrom(buffer_size)
print(modifiedMessage.decode())
clientSocket.close()
