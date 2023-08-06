import socket
import pickle
serverSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
serverSocket.bind(("localhost",8081))
res=[]
while 1:
  rec=serverSocket.recvfrom(4096)
  if not rec:
    break
  data=pickle.loads(rec[0])
  for arr in data:
    boo=0
    for i in range (len(arr)):
      if arr[i]%2:
        boo=1
    if not boo:
      res.append(sum(arr))
  print(res)
  serverSocket.sendto(pickle.dumps(res),rec[1])
serverSocket.close()

