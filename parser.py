import math

stack = []

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

        elif c() in control:

            if control[c()][1]:

                char = c()

                innerCode = ""

                nest = 1
                while pointer + 1 < len(code) or (not c() == ";" or nest > 0):
                    pointer += 1
                    innerCode += c()
                    if c() in control:
                        nest += 1
                    elif c() == ";":
                        nest -= 1
                    if c() == ';' and nest == 1:
                        break
                innerCode = innerCode.rstrip(";")

                parsed.append(("control", control[char][0], parse(innerCode)))

            else:

                parsed.append(("control", control[c()][0]))
            
        pointer += 1

    return parsed

def execute(code):

    pointer = 0
    c = lambda: code[pointer]

    while pointer < len(code):

        if c()[0] == "push":
            stack.append(c()[1])

        elif c()[0] == "function":
            stack.append(c()[1]())

        elif c()[0] == "nonreturn":
            c()[1]()

        elif c()[0] == "setvar":
            if isinstance(scope[c()[1]], list):
                a = pop()
                if type(a) == str:
                    if "|" in a:
                        b = (a.split("|"))
                        for d in b:
                            scope[c()[1]] += [d]
                    else:
                        scope[c()[1]].append(a)
                if type(a) == int or type(a) == float:
                    for b in range(len(to_append)):
                        scope[c()[1]] += [to_append.pop(0)]
                    scope[c()[1]].append(a)
            else:
                scope[c()[1]] = pop()

        elif c()[0] == "getvar":
            stack.append(scope[c()[1]])
            
        elif c()[0] == "control":
            
            if c()[1] == "if":
                
                if pop():
                    execute(c()[2])
                
        print(stack)
        pointer += 1

    if len(stack):print(stack[-1])

# link functions to their characters

digits = list("0123456789")
set_var = list("ABCDEF")
get_var = list("abcdef")

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

control = {'i': ('if', True),
           'w': ('whileLoop', True),
           'B': ('break', False)} # tbc

to_append = []

# vars the user has access to

scope = {'a':0,
         'b':0,
         'c':0,
         'd':0,
         'e':0,
         'f':"Hello World"} # this makes the hello world program nice and short...

code = input("Input code: ")

if code.count('"') % 2 == 1:
    code = '"' + code

instructions = parse(code)
print(instructions)
execute(instructions)
