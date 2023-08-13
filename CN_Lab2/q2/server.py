import socket
import select
import threading
serverSocket=socket.socket()

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(("localhost",8081))
serverSocket.listen()

clients=[]
def send_messages_to_all(message):
  for user in clients:
    user[1].sendall(message.encode())
def listen_messages(client,username):
  while 1:
    msg=client.recv(1024).decode()
    if msg:
      msg_send=username+">"+msg
      send_messages_to_all(msg_send)
def clientHandler(client):
  while 1:
    user=client.recv(1024).decode()
    if user:
      clients.append((user,client))
      break
  threading.Thread(target=listen_messages,args=(client,user,)).start()
while 1:
  client=serverSocket.accept()[0]
  print("Connected to ",client)
  threading.Thread(target=clientHandler,args=(client,)).start()