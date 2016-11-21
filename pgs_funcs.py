''' This is all functions used in PigeonScript for operations, functions, parsing and execution. '''

import math

global stack
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
