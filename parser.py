import math

stack = []

digits = list("0123456789")
set_var = list("ABCDEF")
get_var = list("abcdef")

def cast(data):

    # attempts to convert input from string to int/float.

    if '.' in data:
        try:
            return float(data)
        except:
            return str(data)
    else:
        try:
            return int(data)
        except:
            return str(data)

# Retrieve data from the stack
# When the stack is empty, ask for input

def pop():
    if len(stack):
        return stack.pop()
    else:
        return cast(input("Value required: "))

# Define basic maths functions

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

def factorial():
	i = 1
	for n in range(pop(),1,-1):i*=n
	return i
	
# Various string functions

def indice():
    index = pop()
    item = pop()
    return item[index]

def length():
    return len(pop())

def prnt():
    print(pop())

def pshtoarr():
    to_append.append(pop())

# Boolean operators

def equals():
	return int(pop() == pop())

def morethan():
	return int(pop() > pop())

def lessthan():
	return int(pop() < pop())
	
def booland():
    return int(pop() and pop())

def boolor():
    return int(pop() or pop())

def boolnot():
    return int(not pop())

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
            parsed.append(("push", cast(number)))

        if c() == '"':

            string = ""

            while pointer < len(code):
                string += c()
                pointer += 1
                if pointer >= len(code) or c() == '"':
                    break
            parsed.append(("push", string.strip('"')))

        elif c() in functions:
            parsed.append(("function", functions[c()]))

        elif c() in nonreturn:
            parsed.append(("nonreturn", nonreturn[c()]))

        elif c() in set_var:
            parsed.append(("setvar", c().lower()))

        elif c() in get_var:
            parsed.append(("getvar", c()))

        elif c() in constants:
            parsed.append(("push", constants[c()]))
            
        pointer += 1

    return parsed

# a dict of functions

functions = {'+':add,
             '-':sub,
             '*':mult,
             '/':div,
             '^':exp,
             '%':mod,
             '~':indice,
             'l':length,
	     '=':equals,
	     '>':morethan,
	     '<':lessthan,
	     '&':booland,
             'o':boolor,
             '!':boolnot}

nonreturn = {'p':prnt,
             '|':pshtoarr}

constants = {'g':[]}

control = {} # tbc

to_append = []

# vars the user has access to

scope = {'a':0,
         'b':0,
         'c':0,
         'd':0,
         'e':0,
         'f':"Hello World"}

code = input("Input expression: ")

instructions = parse(code)

print(instructions) # debugging purposes

for i in instructions:

    if i[0] == "push":
        stack.append(i[1])

    elif i[0] == "function":
        stack.append(i[1]())

    elif i[0] == "nonreturn":
        i[1]()

    elif i[0] == "setvar":
        if isinstance(scope[i[1]], list):
            a = pop()
            if type(a) == str:
                if "|" in a:
                    b = (a.split("|"))
                    for c in b:
                        scope[i[1]] += [c]
                else:
                    scope[i[1]].append(a)
            if type(a) == int or type(a) == float:
                for b in range(len(to_append)):
                    scope[i[1]] += [to_append.pop(0)]
                scope[i[1]].append(a)
        else:
            scope[i[1]] = pop()

    elif i[0] == "getvar":
        stack.append(scope[i[1]])

    print(stack) # debugging purposes
