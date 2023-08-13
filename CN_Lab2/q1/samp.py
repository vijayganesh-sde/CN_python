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
print(toPostfix("((1+2)–3*(4/5))+6"))