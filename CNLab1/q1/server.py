import socket
serverSocket=socket.socket()
serverSocket.bind(('127.0.0.1',9090))
serverSocket.listen(2)
datafromClient=""
boo=0
while 1:
  conn=serverSocket.accept()
  if boo:
    conn[0].send(chr(ord(datafromClient)-1).encode())
    break
  else:
    print(conn)   
    datafromClient=conn[0].recv(1024).decode()
    print("data from client1 is",datafromClient)
    conn[0].close()
    boo=1
serverSocket.close()

  