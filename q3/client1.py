import socket
import pickle
import time
c1Socket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
arr1=[3,5,6]
arr2=[4,6,8]
data="hello"
a1=pickle.dumps([arr1,arr2])
c1Socket.sendto(a1,('localhost',8081))
rec=c1Socket.recvfrom(4096)[0]
print(pickle.loads(rec))
c1Socket.close()
