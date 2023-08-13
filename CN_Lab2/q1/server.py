import socket
import pickle
def toPostfix(infix):
    stack = []
    postfix = ""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
    associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '%': 'left', '^': 'right'}
    
    for elem in infix:
        if elem.isalnum():
            postfix += elem
        elif elem == '(':
            stack.append(elem)
        elif elem == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() # discard left parenthesis
        elif elem in precedence:
            while (len(stack) > 0 and stack[-1] in precedence 
                   and (precedence[stack[-1]] > precedence[elem] 
                        or (precedence[stack[-1]] == precedence[elem] 
                            and associativity[elem] == 'left'))):
                postfix += stack.pop()
            stack.append(elem)
    # Retriving postfix notation from stack
    while len(stack) > 0:
        postfix += stack.pop()
    return postfix
serverSocket=socket.socket()
serverSocket.bind(("localhost",8081))
serverSocket.listen(2)
res=[]
while 1:
  rec=serverSocket.accept()[0]
  data=rec.recv(4096).decode()
  print("from client",data)
  if not rec:
    break
  
  res=toPostfix(data)
  print(res)
  rec.send(res.encode())
serverSocket.close()

