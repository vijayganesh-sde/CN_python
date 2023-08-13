import socket
import threading

clientSocket=socket.socket()
clientSocket.connect(('localhost',8081))

def listen_for_messages(client):
  while 1:
    msg=client.recv(1024).decode().split(">")
    if msg:
      user=msg[0]
      message_recv=msg[1]
      print(f"{user}->{message_recv}")
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