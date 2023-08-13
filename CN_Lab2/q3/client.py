import socket
import threading
import pickle
clientSocket=socket.socket()
clientSocket.connect(('localhost',8081))

def listen_for_messages(client):
  while 1:
    msg=client.recv(1024)
    re_data=pickle.loads(msg)
    if msg:
      if len(re_data)==3:
        for arr in re_data:
          print("\n",arr)
      else:
        print(re_data)
def send_to_server(client):
  while 1:
    msg=input("Message: ")
    if msg:
      client.send(msg.encode())
  
def comm_to_server(client):
  user=input("Enter username")
  if user:
    client.send(user.encode())
  
  threading.Thread(target=listen_for_messages,args=(client,)).start()
  send_to_server(client)
  
comm_to_server(clientSocket)