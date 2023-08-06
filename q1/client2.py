import socket
c2Socket=socket.socket()
c2Socket.connect(('localhost',9090))
datafromServer=c2Socket.recv(1024).decode()
print("Data From server",datafromServer)
c2Socket.close()
