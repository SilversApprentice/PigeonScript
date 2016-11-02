import math

stack = []

digits = list("0123456789")
set_var = list("ABCDEF")
get_var = list("abcdef")

# Retrieve data from the stack
# When the stack is empty, ask for input

def pop():
    if len(stack):
        return stack.pop()
    else:
        return float(input("Value required: "))

# Define basic maths operations

def add():
    if len(stack) > 1:
        return pop() + pop()
    else:
        return pop() * 2

def sub():
    if len(stack) > 1:
        return -1 * (pop() - pop())
    else:
        return -1 * pop()

def mult():
    if len(stack) > 1:
        return pop() * pop()
    else:
        return math.pow(pop(), 2)

def div():
    if len(stack) > 1:
        return 1 / (pop() / pop())
    else:
        return 1 / pop()

def exp():
    if len(stack) > 1:
        a = pop()
        b = pop()
        return math.pow(b, a)
    else:
        a = pop()
        return math.pow(a, a)

def mod():
    a,b = pop(),pop()
    return b % a

# Parse the input into a list of instructions

def parse(code):

    pointer = 0

    c = lambda: code[pointer]

    parsed = []

    while pointer < len(code):

        if c() in digits:

            number = ""

            while pointer < len(code) and (c() in digits or (c() == '.' and '.' not in number)):
                number += c()
                pointer += 1
            pointer -= 1
            parsed.append(("pushnum", float(number)))

        elif c() in operations:
            parsed.append(("operation", operations[c()]))

        elif c() in set_var:
            parsed.append(("setvar", c().lower()))

        elif c() in get_var:
            parsed.append(("getvar", c()))
            
        pointer += 1

    return parsed

# a dict of operations

operations = {'+':add,
              '-':sub,
              '*':mult,
              '/':div,
              '^':exp,
              '%':mod}

# vars the user has access to

scope = {'a':0,
         'b':0,
         'c':0,
         'd':0,
         'e':0,
         'f':0}

code = input("Input expression: ")

instructions = parse(code)

print(instructions)

for i in instructions:

    if i[0] == "pushnum":
        stack.append(i[1])

    elif i[0] == "operation":
        stack.append(i[1]())

    elif i[0] == "setvar":
        scope[i[1]] = pop()

    elif i[0] == "getvar":
        stack.append(scope[i[1]])

print(stack[-1])
