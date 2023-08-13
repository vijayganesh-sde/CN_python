import socket
import threading
import pickle
serverSocket=socket.socket()

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(("localhost",8081))
serverSocket.listen()

clients=[]
header_len=10
board=[['','',''],['','',''],['','','']]
def checkWinner(user):
  for i in range (3):
    if board[i][0]==board [i][1]==board[i][2]==user:
      return 1
    if board[0][i]==board [1][i]==board[2][i]==user:
      return 1
  if board[0][0]==board [1][1]==board[2][2]==user:
    return 1
  if board[0][2]==board[1][1]==board[2][0]==user:
    return 1
  return 0
def checkTacToe(value,user):
  posn=list(map(int,value.split()))
  
  if board[posn[0]][posn[1]]=='':
    board[posn[0]][posn[1]]=user
    isWin=checkWinner(user)
    if isWin:
      return pickle.dumps(user+" Wins!!!")
    return pickle.dumps(board)
  else:
    return pickle.dumps("{user} Enters again")
def send_messages_to_all(message):
  for user in clients:
    user[1].send(message)
def listen_messages(client,username):
  while 1:
    msg=client.recv(1024).decode()
    reply=checkTacToe(msg,username)
    if reply:
      
      send_messages_to_all(reply)
def clientHandler(client):
  while 1:
    user=client.recv(1024).decode()
    if user:
      print("Connected to ",user)
      clients.append((user,client))
      break
  threading.Thread(target=listen_messages,args=(client,user,)).start()
while 1:
  client=serverSocket.accept()[0]
  
  threading.Thread(target=clientHandler,args=(client,)).start()