def priorf(c):
    prior = {"+":1, "-":1, "*":2, "/":2}
    return prior.get(c,-1)
    
oper ={"+": lambda a, b: a+b,
       "-": lambda a, b: a-b,
       "*": lambda a, b: a*b,
       "/": lambda a, b: a/b}

def operate (stack, operand):
    num2, num1 = stack.pop(), stack.pop()
    operation = oper[operand]
    res = operation(num1, num2)
    stack.append(res)

s ="9-2+6*2-3*2"
s.strip()
stack =[]
operators = []
i = 0
while True:
    print(s[i])
    if s[i] in "+-*/":
        if operators:
            if priorf(operators[-1]) >= priorf(s[i]) :
                operate(stack, operators.pop())                
                operators.append(s[i])
            else:
                operators.append(s[i])
        else:
            operators.append(s[i])            
        
    else:#if s[i].isdigit():
        stack.append(int(s[i]))
    print(stack)
    print(operators)

    i+=1
            
    if i >= len(s):
        break
    
while operators:
    operate(stack, operators.pop())
print(stack.pop())
