import socket
c1Socket=socket.socket()
c1Socket.connect(('localhost',8081))
data="((1+2)–3*(4/5))+6"
c1Socket.send(data.encode())
rec=c1Socket.recv(4096)
print(rec.decode())
c1Socket.close()
