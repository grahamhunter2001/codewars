def validBraces(string):
    opening=set('([{')
    closing=set(')]}')
    match=set([ ('(',')'), ('[',']'), ('{','}') ])
    stack=[]
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack)==0:
                return False
            lastOpen=stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack)==0
