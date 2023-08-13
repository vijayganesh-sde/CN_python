import socket
serverSocket=socket.socket()
serverSocket.bind(('127.0.0.1',9090))
serverSocket.listen(2)
datafromClient=""
res=None
boo=0
while 1:
  conn=serverSocket.accept()
  if boo:
    conn[0].send(res.encode())
    break
  else:
    print(conn)  
    datafromClient=conn[0].recv(1024).decode()
    print("REcieved in server: ",float(datafromClient))
    res=str(float(datafromClient)+float(datafromClient)**1.5)
    print("Sent data from server: ",res)
    conn[0].close()
    boo=1
serverSocket.close()