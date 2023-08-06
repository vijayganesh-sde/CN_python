import socket
c1Socket=socket.socket()
c1Socket.connect(('localhost',9090))
data=input("Enter character: ")
c1Socket.send(data.encode())
c1Socket.close()
