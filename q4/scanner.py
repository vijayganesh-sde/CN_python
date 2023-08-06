import socket
for port in range(1,1027):
  sock=socket.socket()
  res=sock.connect_ex(('localhost',port))
  if res==0:
    print("Port",port,"is open")
